# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cassandraResourcesCreateUpdateCassandraKeyspace**](DefaultApi.md#cassandraResourcesCreateUpdateCassandraKeyspace) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} |  |
| [**cassandraResourcesCreateUpdateCassandraTable**](DefaultApi.md#cassandraResourcesCreateUpdateCassandraTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} |  |
| [**cassandraResourcesDeleteCassandraKeyspace**](DefaultApi.md#cassandraResourcesDeleteCassandraKeyspace) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} |  |
| [**cassandraResourcesDeleteCassandraTable**](DefaultApi.md#cassandraResourcesDeleteCassandraTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} |  |
| [**cassandraResourcesGetCassandraKeyspace**](DefaultApi.md#cassandraResourcesGetCassandraKeyspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName} |  |
| [**cassandraResourcesGetCassandraKeyspaceThroughput**](DefaultApi.md#cassandraResourcesGetCassandraKeyspaceThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default |  |
| [**cassandraResourcesGetCassandraTable**](DefaultApi.md#cassandraResourcesGetCassandraTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName} |  |
| [**cassandraResourcesGetCassandraTableThroughput**](DefaultApi.md#cassandraResourcesGetCassandraTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default |  |
| [**cassandraResourcesListCassandraKeyspaces**](DefaultApi.md#cassandraResourcesListCassandraKeyspaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces |  |
| [**cassandraResourcesListCassandraTables**](DefaultApi.md#cassandraResourcesListCassandraTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables |  |
| [**cassandraResourcesUpdateCassandraKeyspaceThroughput**](DefaultApi.md#cassandraResourcesUpdateCassandraKeyspaceThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/throughputSettings/default |  |
| [**cassandraResourcesUpdateCassandraTableThroughput**](DefaultApi.md#cassandraResourcesUpdateCassandraTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/cassandraKeyspaces/{keyspaceName}/tables/{tableName}/throughputSettings/default |  |
| [**collectionListMetricDefinitions**](DefaultApi.md#collectionListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metricDefinitions |  |
| [**collectionListMetrics**](DefaultApi.md#collectionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/metrics |  |
| [**collectionListUsages**](DefaultApi.md#collectionListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/usages |  |
| [**collectionPartitionListMetrics**](DefaultApi.md#collectionPartitionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitions/metrics |  |
| [**collectionPartitionListUsages**](DefaultApi.md#collectionPartitionListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitions/usages |  |
| [**collectionPartitionRegionListMetrics**](DefaultApi.md#collectionPartitionRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitions/metrics |  |
| [**collectionRegionListMetrics**](DefaultApi.md#collectionRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/metrics |  |
| [**databaseAccountRegionListMetrics**](DefaultApi.md#databaseAccountRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/metrics |  |
| [**databaseAccountsCheckNameExists**](DefaultApi.md#databaseAccountsCheckNameExists) | **HEAD** /providers/Microsoft.DocumentDB/databaseAccountNames/{accountName} |  |
| [**databaseAccountsCreateOrUpdate**](DefaultApi.md#databaseAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsDelete**](DefaultApi.md#databaseAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsFailoverPriorityChange**](DefaultApi.md#databaseAccountsFailoverPriorityChange) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/failoverPriorityChange |  |
| [**databaseAccountsGet**](DefaultApi.md#databaseAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsGetReadOnlyKeys**](DefaultApi.md#databaseAccountsGetReadOnlyKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys |  |
| [**databaseAccountsList**](DefaultApi.md#databaseAccountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/databaseAccounts |  |
| [**databaseAccountsListByResourceGroup**](DefaultApi.md#databaseAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts |  |
| [**databaseAccountsListConnectionStrings**](DefaultApi.md#databaseAccountsListConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listConnectionStrings |  |
| [**databaseAccountsListKeys**](DefaultApi.md#databaseAccountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listKeys |  |
| [**databaseAccountsListMetricDefinitions**](DefaultApi.md#databaseAccountsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metricDefinitions |  |
| [**databaseAccountsListMetrics**](DefaultApi.md#databaseAccountsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metrics |  |
| [**databaseAccountsListReadOnlyKeys**](DefaultApi.md#databaseAccountsListReadOnlyKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys |  |
| [**databaseAccountsListUsages**](DefaultApi.md#databaseAccountsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/usages |  |
| [**databaseAccountsOfflineRegion**](DefaultApi.md#databaseAccountsOfflineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/offlineRegion |  |
| [**databaseAccountsOnlineRegion**](DefaultApi.md#databaseAccountsOnlineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/onlineRegion |  |
| [**databaseAccountsRegenerateKey**](DefaultApi.md#databaseAccountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/regenerateKey |  |
| [**databaseAccountsUpdate**](DefaultApi.md#databaseAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseListMetricDefinitions**](DefaultApi.md#databaseListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metricDefinitions |  |
| [**databaseListMetrics**](DefaultApi.md#databaseListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metrics |  |
| [**databaseListUsages**](DefaultApi.md#databaseListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/usages |  |
| [**gremlinResourcesCreateUpdateGremlinDatabase**](DefaultApi.md#gremlinResourcesCreateUpdateGremlinDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} |  |
| [**gremlinResourcesCreateUpdateGremlinGraph**](DefaultApi.md#gremlinResourcesCreateUpdateGremlinGraph) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} |  |
| [**gremlinResourcesDeleteGremlinDatabase**](DefaultApi.md#gremlinResourcesDeleteGremlinDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} |  |
| [**gremlinResourcesDeleteGremlinGraph**](DefaultApi.md#gremlinResourcesDeleteGremlinGraph) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} |  |
| [**gremlinResourcesGetGremlinDatabase**](DefaultApi.md#gremlinResourcesGetGremlinDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName} |  |
| [**gremlinResourcesGetGremlinDatabaseThroughput**](DefaultApi.md#gremlinResourcesGetGremlinDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default |  |
| [**gremlinResourcesGetGremlinGraph**](DefaultApi.md#gremlinResourcesGetGremlinGraph) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName} |  |
| [**gremlinResourcesGetGremlinGraphThroughput**](DefaultApi.md#gremlinResourcesGetGremlinGraphThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default |  |
| [**gremlinResourcesListGremlinDatabases**](DefaultApi.md#gremlinResourcesListGremlinDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases |  |
| [**gremlinResourcesListGremlinGraphs**](DefaultApi.md#gremlinResourcesListGremlinGraphs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs |  |
| [**gremlinResourcesUpdateGremlinDatabaseThroughput**](DefaultApi.md#gremlinResourcesUpdateGremlinDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/throughputSettings/default |  |
| [**gremlinResourcesUpdateGremlinGraphThroughput**](DefaultApi.md#gremlinResourcesUpdateGremlinGraphThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/gremlinDatabases/{databaseName}/graphs/{graphName}/throughputSettings/default |  |
| [**mongoDBResourcesCreateUpdateMongoDBCollection**](DefaultApi.md#mongoDBResourcesCreateUpdateMongoDBCollection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} |  |
| [**mongoDBResourcesCreateUpdateMongoDBDatabase**](DefaultApi.md#mongoDBResourcesCreateUpdateMongoDBDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} |  |
| [**mongoDBResourcesDeleteMongoDBCollection**](DefaultApi.md#mongoDBResourcesDeleteMongoDBCollection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} |  |
| [**mongoDBResourcesDeleteMongoDBDatabase**](DefaultApi.md#mongoDBResourcesDeleteMongoDBDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} |  |
| [**mongoDBResourcesGetMongoDBCollection**](DefaultApi.md#mongoDBResourcesGetMongoDBCollection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName} |  |
| [**mongoDBResourcesGetMongoDBCollectionThroughput**](DefaultApi.md#mongoDBResourcesGetMongoDBCollectionThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default |  |
| [**mongoDBResourcesGetMongoDBDatabase**](DefaultApi.md#mongoDBResourcesGetMongoDBDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName} |  |
| [**mongoDBResourcesGetMongoDBDatabaseThroughput**](DefaultApi.md#mongoDBResourcesGetMongoDBDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default |  |
| [**mongoDBResourcesListMongoDBCollections**](DefaultApi.md#mongoDBResourcesListMongoDBCollections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections |  |
| [**mongoDBResourcesListMongoDBDatabases**](DefaultApi.md#mongoDBResourcesListMongoDBDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases |  |
| [**mongoDBResourcesUpdateMongoDBCollectionThroughput**](DefaultApi.md#mongoDBResourcesUpdateMongoDBCollectionThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/collections/{collectionName}/throughputSettings/default |  |
| [**mongoDBResourcesUpdateMongoDBDatabaseThroughput**](DefaultApi.md#mongoDBResourcesUpdateMongoDBDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/mongodbDatabases/{databaseName}/throughputSettings/default |  |
| [**partitionKeyRangeIdListMetrics**](DefaultApi.md#partitionKeyRangeIdListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics |  |
| [**partitionKeyRangeIdRegionListMetrics**](DefaultApi.md#partitionKeyRangeIdRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics |  |
| [**percentileListMetrics**](DefaultApi.md#percentileListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/percentile/metrics |  |
| [**percentileSourceTargetListMetrics**](DefaultApi.md#percentileSourceTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sourceRegion/{sourceRegion}/targetRegion/{targetRegion}/percentile/metrics |  |
| [**percentileTargetListMetrics**](DefaultApi.md#percentileTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/targetRegion/{targetRegion}/percentile/metrics |  |
| [**sqlResourcesCreateUpdateSqlContainer**](DefaultApi.md#sqlResourcesCreateUpdateSqlContainer) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} |  |
| [**sqlResourcesCreateUpdateSqlDatabase**](DefaultApi.md#sqlResourcesCreateUpdateSqlDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} |  |
| [**sqlResourcesCreateUpdateSqlStoredProcedure**](DefaultApi.md#sqlResourcesCreateUpdateSqlStoredProcedure) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} |  |
| [**sqlResourcesCreateUpdateSqlTrigger**](DefaultApi.md#sqlResourcesCreateUpdateSqlTrigger) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} |  |
| [**sqlResourcesCreateUpdateSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesCreateUpdateSqlUserDefinedFunction) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} |  |
| [**sqlResourcesDeleteSqlContainer**](DefaultApi.md#sqlResourcesDeleteSqlContainer) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} |  |
| [**sqlResourcesDeleteSqlDatabase**](DefaultApi.md#sqlResourcesDeleteSqlDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} |  |
| [**sqlResourcesDeleteSqlStoredProcedure**](DefaultApi.md#sqlResourcesDeleteSqlStoredProcedure) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} |  |
| [**sqlResourcesDeleteSqlTrigger**](DefaultApi.md#sqlResourcesDeleteSqlTrigger) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} |  |
| [**sqlResourcesDeleteSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesDeleteSqlUserDefinedFunction) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} |  |
| [**sqlResourcesGetSqlContainer**](DefaultApi.md#sqlResourcesGetSqlContainer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName} |  |
| [**sqlResourcesGetSqlContainerThroughput**](DefaultApi.md#sqlResourcesGetSqlContainerThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default |  |
| [**sqlResourcesGetSqlDatabase**](DefaultApi.md#sqlResourcesGetSqlDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName} |  |
| [**sqlResourcesGetSqlDatabaseThroughput**](DefaultApi.md#sqlResourcesGetSqlDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default |  |
| [**sqlResourcesGetSqlStoredProcedure**](DefaultApi.md#sqlResourcesGetSqlStoredProcedure) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures/{storedProcedureName} |  |
| [**sqlResourcesGetSqlTrigger**](DefaultApi.md#sqlResourcesGetSqlTrigger) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers/{triggerName} |  |
| [**sqlResourcesGetSqlUserDefinedFunction**](DefaultApi.md#sqlResourcesGetSqlUserDefinedFunction) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions/{userDefinedFunctionName} |  |
| [**sqlResourcesListSqlContainers**](DefaultApi.md#sqlResourcesListSqlContainers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers |  |
| [**sqlResourcesListSqlDatabases**](DefaultApi.md#sqlResourcesListSqlDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases |  |
| [**sqlResourcesListSqlStoredProcedures**](DefaultApi.md#sqlResourcesListSqlStoredProcedures) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/storedProcedures |  |
| [**sqlResourcesListSqlTriggers**](DefaultApi.md#sqlResourcesListSqlTriggers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/triggers |  |
| [**sqlResourcesListSqlUserDefinedFunctions**](DefaultApi.md#sqlResourcesListSqlUserDefinedFunctions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/userDefinedFunctions |  |
| [**sqlResourcesUpdateSqlContainerThroughput**](DefaultApi.md#sqlResourcesUpdateSqlContainerThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/containers/{containerName}/throughputSettings/default |  |
| [**sqlResourcesUpdateSqlDatabaseThroughput**](DefaultApi.md#sqlResourcesUpdateSqlDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sqlDatabases/{databaseName}/throughputSettings/default |  |
| [**tableResourcesCreateUpdateTable**](DefaultApi.md#tableResourcesCreateUpdateTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} |  |
| [**tableResourcesDeleteTable**](DefaultApi.md#tableResourcesDeleteTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} |  |
| [**tableResourcesGetTable**](DefaultApi.md#tableResourcesGetTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName} |  |
| [**tableResourcesGetTableThroughput**](DefaultApi.md#tableResourcesGetTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default |  |
| [**tableResourcesListTables**](DefaultApi.md#tableResourcesListTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables |  |
| [**tableResourcesUpdateTableThroughput**](DefaultApi.md#tableResourcesUpdateTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/tables/{tableName}/throughputSettings/default |  |


<a id="cassandraResourcesCreateUpdateCassandraKeyspace"></a>
# **cassandraResourcesCreateUpdateCassandraKeyspace**
> CassandraKeyspaceGetResults cassandraResourcesCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters)



Create or update an Azure Cosmos DB Cassandra keyspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    CassandraKeyspaceCreateUpdateParameters createUpdateCassandraKeyspaceParameters = new CassandraKeyspaceCreateUpdateParameters(); // CassandraKeyspaceCreateUpdateParameters | The parameters to provide for the current Cassandra keyspace.
    try {
      CassandraKeyspaceGetResults result = apiInstance.cassandraResourcesCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesCreateUpdateCassandraKeyspace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateCassandraKeyspaceParameters** | [**CassandraKeyspaceCreateUpdateParameters**](CassandraKeyspaceCreateUpdateParameters.md)| The parameters to provide for the current Cassandra keyspace. | |

### Return type

[**CassandraKeyspaceGetResults**](CassandraKeyspaceGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra keyspace create or update operation was completed successfully. |  -  |
| **202** | The Cassandra keyspace create or update operation will complete asynchronously. |  -  |

<a id="cassandraResourcesCreateUpdateCassandraTable"></a>
# **cassandraResourcesCreateUpdateCassandraTable**
> CassandraTableGetResults cassandraResourcesCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters)



Create or update an Azure Cosmos DB Cassandra Table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    CassandraTableCreateUpdateParameters createUpdateCassandraTableParameters = new CassandraTableCreateUpdateParameters(); // CassandraTableCreateUpdateParameters | The parameters to provide for the current Cassandra Table.
    try {
      CassandraTableGetResults result = apiInstance.cassandraResourcesCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesCreateUpdateCassandraTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateCassandraTableParameters** | [**CassandraTableCreateUpdateParameters**](CassandraTableCreateUpdateParameters.md)| The parameters to provide for the current Cassandra Table. | |

### Return type

[**CassandraTableGetResults**](CassandraTableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra Table create or update operation was completed successfully. |  -  |
| **202** | The Cassandra Table create or update operation will complete asynchronously. |  -  |

<a id="cassandraResourcesDeleteCassandraKeyspace"></a>
# **cassandraResourcesDeleteCassandraKeyspace**
> cassandraResourcesDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Deletes an existing Azure Cosmos DB Cassandra keyspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.cassandraResourcesDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesDeleteCassandraKeyspace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The Cassandra keyspace delete operation will complete asynchronously. |  -  |
| **204** | The Cassandra keyspace delete operation was completed successfully. |  -  |

<a id="cassandraResourcesDeleteCassandraTable"></a>
# **cassandraResourcesDeleteCassandraTable**
> cassandraResourcesDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Deletes an existing Azure Cosmos DB Cassandra table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.cassandraResourcesDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesDeleteCassandraTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The Cassandra table delete operation will complete asynchronously. |  -  |
| **204** | The Cassandra table delete operation was completed successfully. |  -  |

<a id="cassandraResourcesGetCassandraKeyspace"></a>
# **cassandraResourcesGetCassandraKeyspace**
> CassandraKeyspaceGetResults cassandraResourcesGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Gets the Cassandra keyspaces under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      CassandraKeyspaceGetResults result = apiInstance.cassandraResourcesGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesGetCassandraKeyspace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**CassandraKeyspaceGetResults**](CassandraKeyspaceGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra keyspace property was retrieved successfully. |  -  |

<a id="cassandraResourcesGetCassandraKeyspaceThroughput"></a>
# **cassandraResourcesGetCassandraKeyspaceThroughput**
> ThroughputSettingsGetResults cassandraResourcesGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Gets the RUs per second of the Cassandra Keyspace under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.cassandraResourcesGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesGetCassandraKeyspaceThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra Keyspace was retrieved successfully. |  -  |

<a id="cassandraResourcesGetCassandraTable"></a>
# **cassandraResourcesGetCassandraTable**
> CassandraTableGetResults cassandraResourcesGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Gets the Cassandra table under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      CassandraTableGetResults result = apiInstance.cassandraResourcesGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesGetCassandraTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**CassandraTableGetResults**](CassandraTableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra table property was retrieved successfully. |  -  |

<a id="cassandraResourcesGetCassandraTableThroughput"></a>
# **cassandraResourcesGetCassandraTableThroughput**
> ThroughputSettingsGetResults cassandraResourcesGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



Gets the RUs per second of the Cassandra table under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.cassandraResourcesGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesGetCassandraTableThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra table was retrieved successfully. |  -  |

<a id="cassandraResourcesListCassandraKeyspaces"></a>
# **cassandraResourcesListCassandraKeyspaces**
> CassandraKeyspaceListResult cassandraResourcesListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Cassandra keyspaces under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      CassandraKeyspaceListResult result = apiInstance.cassandraResourcesListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesListCassandraKeyspaces");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**CassandraKeyspaceListResult**](CassandraKeyspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra keyspace properties were retrieved successfully. |  -  |

<a id="cassandraResourcesListCassandraTables"></a>
# **cassandraResourcesListCassandraTables**
> CassandraTableListResult cassandraResourcesListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



Lists the Cassandra table under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      CassandraTableListResult result = apiInstance.cassandraResourcesListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesListCassandraTables");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**CassandraTableListResult**](CassandraTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra table properties were retrieved successfully. |  -  |

<a id="cassandraResourcesUpdateCassandraKeyspaceThroughput"></a>
# **cassandraResourcesUpdateCassandraKeyspaceThroughput**
> ThroughputSettingsGetResults cassandraResourcesUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Cassandra Keyspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra Keyspace.
    try {
      ThroughputSettingsGetResults result = apiInstance.cassandraResourcesUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesUpdateCassandraKeyspaceThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra Keyspace. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra Keyspace update operation was completed successfully. |  -  |
| **202** | The RUs per second of the Cassandra Keyspace update operation will complete asynchronously. |  -  |

<a id="cassandraResourcesUpdateCassandraTableThroughput"></a>
# **cassandraResourcesUpdateCassandraTableThroughput**
> ThroughputSettingsGetResults cassandraResourcesUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Cassandra table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String keyspaceName = "keyspaceName_example"; // String | Cosmos DB keyspace name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra table.
    try {
      ThroughputSettingsGetResults result = apiInstance.cassandraResourcesUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cassandraResourcesUpdateCassandraTableThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **keyspaceName** | **String**| Cosmos DB keyspace name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra table. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra table update operation was completed successfully. |  -  |
| **202** | The RUs per second of the Cassandra table update operation will complete asynchronously. |  -  |

<a id="collectionListMetricDefinitions"></a>
# **collectionListMetricDefinitions**
> MetricDefinitionsListResult collectionListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion)



Retrieves metric definitions for the given collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MetricDefinitionsListResult result = apiInstance.collectionListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionListMetricDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric definitions for the collection were retrieved successfully. |  -  |

<a id="collectionListMetrics"></a>
# **collectionListMetrics**
> MetricListResult collectionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account and collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      MetricListResult result = apiInstance.collectionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics for the database account were retrieved successfully. |  -  |

<a id="collectionListUsages"></a>
# **collectionListUsages**
> UsagesResult collectionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the usages (most recent storage data) for the given collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    try {
      UsagesResult result = apiInstance.collectionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionListUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] |

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The usages for the collection were retrieved successfully. |  -  |

<a id="collectionPartitionListMetrics"></a>
# **collectionPartitionListMetrics**
> PartitionMetricListResult collectionPartitionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given collection, split by partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PartitionMetricListResult result = apiInstance.collectionPartitionListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionPartitionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition-level metrics for the collection were retrieved successfully. |  -  |

<a id="collectionPartitionListUsages"></a>
# **collectionPartitionListUsages**
> PartitionUsagesResult collectionPartitionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the usages (most recent storage data) for the given collection, split by partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    try {
      PartitionUsagesResult result = apiInstance.collectionPartitionListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionPartitionListUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] |

### Return type

[**PartitionUsagesResult**](PartitionUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The usages for the collection, per partition were retrieved successfully. |  -  |

<a id="collectionPartitionRegionListMetrics"></a>
# **collectionPartitionRegionListMetrics**
> PartitionMetricListResult collectionPartitionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given collection and region, split by partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PartitionMetricListResult result = apiInstance.collectionPartitionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionPartitionRegionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition-level metrics for the collection and region were retrieved successfully. |  -  |

<a id="collectionRegionListMetrics"></a>
# **collectionRegionListMetrics**
> MetricListResult collectionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account, collection and region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      MetricListResult result = apiInstance.collectionRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#collectionRegionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics for the database account were retrieved successfully. |  -  |

<a id="databaseAccountRegionListMetrics"></a>
# **databaseAccountRegionListMetrics**
> MetricListResult databaseAccountRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account and region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      MetricListResult result = apiInstance.databaseAccountRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountRegionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics for the database account were retrieved successfully. |  -  |

<a id="databaseAccountsCheckNameExists"></a>
# **databaseAccountsCheckNameExists**
> databaseAccountsCheckNameExists(accountName, apiVersion)



Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the &#39;-&#39; character, and must be between 3 and 50 characters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.databaseAccountsCheckNameExists(accountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCheckNameExists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The account name is valid but is already in use. |  -  |
| **404** | Not Found. The account name is available and valid. |  -  |

<a id="databaseAccountsCreateOrUpdate"></a>
# **databaseAccountsCreateOrUpdate**
> DatabaseAccountGetResults databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters)



Creates or updates an Azure Cosmos DB database account. The \&quot;Update\&quot; method is preferred when performing updates on an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    DatabaseAccountCreateUpdateParameters createUpdateParameters = new DatabaseAccountCreateUpdateParameters(); // DatabaseAccountCreateUpdateParameters | The parameters to provide for the current database account.
    try {
      DatabaseAccountGetResults result = apiInstance.databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateOrUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateParameters** | [**DatabaseAccountCreateUpdateParameters**](DatabaseAccountCreateUpdateParameters.md)| The parameters to provide for the current database account. | |

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database account create or update operation will complete asynchronously. |  -  |

<a id="databaseAccountsDelete"></a>
# **databaseAccountsDelete**
> databaseAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Deletes an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.databaseAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The database account delete operation will complete asynchronously. |  -  |
| **204** | The specified account does not exist in the subscription. |  -  |

<a id="databaseAccountsFailoverPriorityChange"></a>
# **databaseAccountsFailoverPriorityChange**
> databaseAccountsFailoverPriorityChange(subscriptionId, resourceGroupName, accountName, apiVersion, failoverParameters)



Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority &#x3D; (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    FailoverPolicies failoverParameters = new FailoverPolicies(); // FailoverPolicies | The new failover policies for the database account.
    try {
      apiInstance.databaseAccountsFailoverPriorityChange(subscriptionId, resourceGroupName, accountName, apiVersion, failoverParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsFailoverPriorityChange");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **failoverParameters** | [**FailoverPolicies**](FailoverPolicies.md)| The new failover policies for the database account. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. The failover policy change operation will complete asynchronously. |  -  |
| **204** | No Content |  -  |

<a id="databaseAccountsGet"></a>
# **databaseAccountsGet**
> DatabaseAccountGetResults databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieves the properties of an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      DatabaseAccountGetResults result = apiInstance.databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database account properties were retrieved successfully. |  -  |

<a id="databaseAccountsGetReadOnlyKeys"></a>
# **databaseAccountsGetReadOnlyKeys**
> DatabaseAccountListReadOnlyKeysResult databaseAccountsGetReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the read-only access keys for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      DatabaseAccountListReadOnlyKeysResult result = apiInstance.databaseAccountsGetReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetReadOnlyKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsList"></a>
# **databaseAccountsList**
> DatabaseAccountsListResult databaseAccountsList(apiVersion, subscriptionId)



Lists all the Azure Cosmos DB database accounts available under the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    try {
      DatabaseAccountsListResult result = apiInstance.databaseAccountsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **subscriptionId** | **String**| Azure subscription ID. | |

### Return type

[**DatabaseAccountsListResult**](DatabaseAccountsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsListByResourceGroup"></a>
# **databaseAccountsListByResourceGroup**
> DatabaseAccountsListResult databaseAccountsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all the Azure Cosmos DB database accounts available under the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    try {
      DatabaseAccountsListResult result = apiInstance.databaseAccountsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListByResourceGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **subscriptionId** | **String**| Azure subscription ID. | |

### Return type

[**DatabaseAccountsListResult**](DatabaseAccountsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsListConnectionStrings"></a>
# **databaseAccountsListConnectionStrings**
> DatabaseAccountListConnectionStringsResult databaseAccountsListConnectionStrings(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the connection strings for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      DatabaseAccountListConnectionStringsResult result = apiInstance.databaseAccountsListConnectionStrings(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListConnectionStrings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**DatabaseAccountListConnectionStringsResult**](DatabaseAccountListConnectionStringsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsListKeys"></a>
# **databaseAccountsListKeys**
> DatabaseAccountListKeysResult databaseAccountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the access keys for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      DatabaseAccountListKeysResult result = apiInstance.databaseAccountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**DatabaseAccountListKeysResult**](DatabaseAccountListKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsListMetricDefinitions"></a>
# **databaseAccountsListMetricDefinitions**
> MetricDefinitionsListResult databaseAccountsListMetricDefinitions(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieves metric definitions for the given database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MetricDefinitionsListResult result = apiInstance.databaseAccountsListMetricDefinitions(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListMetricDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric definitions for the database account were retrieved successfully. |  -  |

<a id="databaseAccountsListMetrics"></a>
# **databaseAccountsListMetrics**
> MetricListResult databaseAccountsListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      MetricListResult result = apiInstance.databaseAccountsListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics for the database account were retrieved successfully. |  -  |

<a id="databaseAccountsListReadOnlyKeys"></a>
# **databaseAccountsListReadOnlyKeys**
> DatabaseAccountListReadOnlyKeysResult databaseAccountsListReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the read-only access keys for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      DatabaseAccountListReadOnlyKeysResult result = apiInstance.databaseAccountsListReadOnlyKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListReadOnlyKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="databaseAccountsListUsages"></a>
# **databaseAccountsListUsages**
> UsagesResult databaseAccountsListUsages(subscriptionId, resourceGroupName, accountName, apiVersion, $filter)



Retrieves the usages (most recent data) for the given database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    try {
      UsagesResult result = apiInstance.databaseAccountsListUsages(subscriptionId, resourceGroupName, accountName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] |

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The usages for the database account were retrieved successfully. |  -  |

<a id="databaseAccountsOfflineRegion"></a>
# **databaseAccountsOfflineRegion**
> databaseAccountsOfflineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOffline)



Offline the specified region for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    RegionForOnlineOffline regionParameterForOffline = new RegionForOnlineOffline(); // RegionForOnlineOffline | Cosmos DB region to offline for the database account.
    try {
      apiInstance.databaseAccountsOfflineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOffline);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsOfflineRegion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **regionParameterForOffline** | [**RegionForOnlineOffline**](RegionForOnlineOffline.md)| Cosmos DB region to offline for the database account. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The offline region operation is completed successfully. |  -  |
| **202** | Accepted. The offline region operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databaseAccountsOnlineRegion"></a>
# **databaseAccountsOnlineRegion**
> databaseAccountsOnlineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOnline)



Online the specified region for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    RegionForOnlineOffline regionParameterForOnline = new RegionForOnlineOffline(); // RegionForOnlineOffline | Cosmos DB region to online for the database account.
    try {
      apiInstance.databaseAccountsOnlineRegion(subscriptionId, resourceGroupName, accountName, apiVersion, regionParameterForOnline);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsOnlineRegion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **regionParameterForOnline** | [**RegionForOnlineOffline**](RegionForOnlineOffline.md)| Cosmos DB region to online for the database account. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The online region operation is completed successfully. |  -  |
| **202** | Accepted. The online region operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databaseAccountsRegenerateKey"></a>
# **databaseAccountsRegenerateKey**
> databaseAccountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, keyToRegenerate)



Regenerates an access key for the specified Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    DatabaseAccountRegenerateKeyParameters keyToRegenerate = new DatabaseAccountRegenerateKeyParameters(); // DatabaseAccountRegenerateKeyParameters | The name of the key to regenerate.
    try {
      apiInstance.databaseAccountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, keyToRegenerate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsRegenerateKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **keyToRegenerate** | [**DatabaseAccountRegenerateKeyParameters**](DatabaseAccountRegenerateKeyParameters.md)| The name of the key to regenerate. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted. The regenerate key operation will complete asynchronously. |  -  |

<a id="databaseAccountsUpdate"></a>
# **databaseAccountsUpdate**
> DatabaseAccountGetResults databaseAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters)



Updates the properties of an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    DatabaseAccountUpdateParameters updateParameters = new DatabaseAccountUpdateParameters(); // DatabaseAccountUpdateParameters | The parameters to provide for the current database account.
    try {
      DatabaseAccountGetResults result = apiInstance.databaseAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateParameters** | [**DatabaseAccountUpdateParameters**](DatabaseAccountUpdateParameters.md)| The parameters to provide for the current database account. | |

### Return type

[**DatabaseAccountGetResults**](DatabaseAccountGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database account update operation will complete asynchronously. |  -  |

<a id="databaseListMetricDefinitions"></a>
# **databaseListMetricDefinitions**
> MetricDefinitionsListResult databaseListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion)



Retrieves metric definitions for the given database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MetricDefinitionsListResult result = apiInstance.databaseListMetricDefinitions(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseListMetricDefinitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MetricDefinitionsListResult**](MetricDefinitionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric definitions for the database were retrieved successfully. |  -  |

<a id="databaseListMetrics"></a>
# **databaseListMetrics**
> MetricListResult databaseListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account and database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      MetricListResult result = apiInstance.databaseListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics for the database account were retrieved successfully. |  -  |

<a id="databaseListUsages"></a>
# **databaseListUsages**
> UsagesResult databaseListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, $filter)



Retrieves the usages (most recent data) for the given database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names).
    try {
      UsagesResult result = apiInstance.databaseListUsages(subscriptionId, resourceGroupName, accountName, databaseRid, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseListUsages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] |

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The usages for the database were retrieved successfully. |  -  |

<a id="gremlinResourcesCreateUpdateGremlinDatabase"></a>
# **gremlinResourcesCreateUpdateGremlinDatabase**
> GremlinDatabaseGetResults gremlinResourcesCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters)



Create or update an Azure Cosmos DB Gremlin database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    GremlinDatabaseCreateUpdateParameters createUpdateGremlinDatabaseParameters = new GremlinDatabaseCreateUpdateParameters(); // GremlinDatabaseCreateUpdateParameters | The parameters to provide for the current Gremlin database.
    try {
      GremlinDatabaseGetResults result = apiInstance.gremlinResourcesCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesCreateUpdateGremlinDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateGremlinDatabaseParameters** | [**GremlinDatabaseCreateUpdateParameters**](GremlinDatabaseCreateUpdateParameters.md)| The parameters to provide for the current Gremlin database. | |

### Return type

[**GremlinDatabaseGetResults**](GremlinDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin database create or update operation was completed successfully. |  -  |
| **202** | The Gremlin database create or update operation will complete asynchronously. |  -  |

<a id="gremlinResourcesCreateUpdateGremlinGraph"></a>
# **gremlinResourcesCreateUpdateGremlinGraph**
> GremlinGraphGetResults gremlinResourcesCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters)



Create or update an Azure Cosmos DB Gremlin graph

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String graphName = "graphName_example"; // String | Cosmos DB graph name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    GremlinGraphCreateUpdateParameters createUpdateGremlinGraphParameters = new GremlinGraphCreateUpdateParameters(); // GremlinGraphCreateUpdateParameters | The parameters to provide for the current Gremlin graph.
    try {
      GremlinGraphGetResults result = apiInstance.gremlinResourcesCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesCreateUpdateGremlinGraph");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **graphName** | **String**| Cosmos DB graph name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateGremlinGraphParameters** | [**GremlinGraphCreateUpdateParameters**](GremlinGraphCreateUpdateParameters.md)| The parameters to provide for the current Gremlin graph. | |

### Return type

[**GremlinGraphGetResults**](GremlinGraphGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin graph create or update operation was completed successfully. |  -  |
| **202** | The Gremlin graph create or update operation will complete asynchronously. |  -  |

<a id="gremlinResourcesDeleteGremlinDatabase"></a>
# **gremlinResourcesDeleteGremlinDatabase**
> gremlinResourcesDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB Gremlin database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.gremlinResourcesDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesDeleteGremlinDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The Gremlin database delete operation will complete asynchronously. |  -  |
| **204** | The Gremlin database delete operation was completed successfully. |  -  |

<a id="gremlinResourcesDeleteGremlinGraph"></a>
# **gremlinResourcesDeleteGremlinGraph**
> gremlinResourcesDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Deletes an existing Azure Cosmos DB Gremlin graph.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String graphName = "graphName_example"; // String | Cosmos DB graph name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.gremlinResourcesDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesDeleteGremlinGraph");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **graphName** | **String**| Cosmos DB graph name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The Gremlin graph delete operation will complete asynchronously. |  -  |
| **204** | The Gremlin graph delete operation was completed successfully. |  -  |

<a id="gremlinResourcesGetGremlinDatabase"></a>
# **gremlinResourcesGetGremlinDatabase**
> GremlinDatabaseGetResults gremlinResourcesGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the Gremlin databases under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      GremlinDatabaseGetResults result = apiInstance.gremlinResourcesGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesGetGremlinDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**GremlinDatabaseGetResults**](GremlinDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin database property was retrieved successfully. |  -  |

<a id="gremlinResourcesGetGremlinDatabaseThroughput"></a>
# **gremlinResourcesGetGremlinDatabaseThroughput**
> ThroughputSettingsGetResults gremlinResourcesGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.gremlinResourcesGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesGetGremlinDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin database was retrieved successfully. |  -  |

<a id="gremlinResourcesGetGremlinGraph"></a>
# **gremlinResourcesGetGremlinGraph**
> GremlinGraphGetResults gremlinResourcesGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Gets the Gremlin graph under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String graphName = "graphName_example"; // String | Cosmos DB graph name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      GremlinGraphGetResults result = apiInstance.gremlinResourcesGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesGetGremlinGraph");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **graphName** | **String**| Cosmos DB graph name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**GremlinGraphGetResults**](GremlinGraphGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin graph property was retrieved successfully. |  -  |

<a id="gremlinResourcesGetGremlinGraphThroughput"></a>
# **gremlinResourcesGetGremlinGraphThroughput**
> ThroughputSettingsGetResults gremlinResourcesGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



Gets the Gremlin graph throughput under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String graphName = "graphName_example"; // String | Cosmos DB graph name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.gremlinResourcesGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesGetGremlinGraphThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **graphName** | **String**| Cosmos DB graph name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin graph was retrieved successfully. |  -  |

<a id="gremlinResourcesListGremlinDatabases"></a>
# **gremlinResourcesListGremlinDatabases**
> GremlinDatabaseListResult gremlinResourcesListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Gremlin databases under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      GremlinDatabaseListResult result = apiInstance.gremlinResourcesListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesListGremlinDatabases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**GremlinDatabaseListResult**](GremlinDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin database properties were retrieved successfully. |  -  |

<a id="gremlinResourcesListGremlinGraphs"></a>
# **gremlinResourcesListGremlinGraphs**
> GremlinGraphListResult gremlinResourcesListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the Gremlin graph under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      GremlinGraphListResult result = apiInstance.gremlinResourcesListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesListGremlinGraphs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**GremlinGraphListResult**](GremlinGraphListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin graph properties were retrieved successfully. |  -  |

<a id="gremlinResourcesUpdateGremlinDatabaseThroughput"></a>
# **gremlinResourcesUpdateGremlinDatabaseThroughput**
> ThroughputSettingsGetResults gremlinResourcesUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Gremlin database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin database.
    try {
      ThroughputSettingsGetResults result = apiInstance.gremlinResourcesUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesUpdateGremlinDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin database. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin database update operation was completed successfully. |  -  |
| **202** | The RUs per second of the Gremlin database update operation will complete asynchronously. |  -  |

<a id="gremlinResourcesUpdateGremlinGraphThroughput"></a>
# **gremlinResourcesUpdateGremlinGraphThroughput**
> ThroughputSettingsGetResults gremlinResourcesUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Gremlin graph

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String graphName = "graphName_example"; // String | Cosmos DB graph name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin graph.
    try {
      ThroughputSettingsGetResults result = apiInstance.gremlinResourcesUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#gremlinResourcesUpdateGremlinGraphThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **graphName** | **String**| Cosmos DB graph name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin graph. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin graph update operation was completed successfully. |  -  |
| **202** | The RUs per second of the Gremlin graph update operation will complete asynchronously. |  -  |

<a id="mongoDBResourcesCreateUpdateMongoDBCollection"></a>
# **mongoDBResourcesCreateUpdateMongoDBCollection**
> MongoDBCollectionGetResults mongoDBResourcesCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters)



Create or update an Azure Cosmos DB MongoDB Collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String collectionName = "collectionName_example"; // String | Cosmos DB collection name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    MongoDBCollectionCreateUpdateParameters createUpdateMongoDBCollectionParameters = new MongoDBCollectionCreateUpdateParameters(); // MongoDBCollectionCreateUpdateParameters | The parameters to provide for the current MongoDB Collection.
    try {
      MongoDBCollectionGetResults result = apiInstance.mongoDBResourcesCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesCreateUpdateMongoDBCollection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **collectionName** | **String**| Cosmos DB collection name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateMongoDBCollectionParameters** | [**MongoDBCollectionCreateUpdateParameters**](MongoDBCollectionCreateUpdateParameters.md)| The parameters to provide for the current MongoDB Collection. | |

### Return type

[**MongoDBCollectionGetResults**](MongoDBCollectionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB Collection create or update operation was completed successfully. |  -  |
| **202** | The MongoDB Collection create or update operation will complete asynchronously. |  -  |

<a id="mongoDBResourcesCreateUpdateMongoDBDatabase"></a>
# **mongoDBResourcesCreateUpdateMongoDBDatabase**
> MongoDBDatabaseGetResults mongoDBResourcesCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters)



Create or updates Azure Cosmos DB MongoDB database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    MongoDBDatabaseCreateUpdateParameters createUpdateMongoDBDatabaseParameters = new MongoDBDatabaseCreateUpdateParameters(); // MongoDBDatabaseCreateUpdateParameters | The parameters to provide for the current MongoDB database.
    try {
      MongoDBDatabaseGetResults result = apiInstance.mongoDBResourcesCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesCreateUpdateMongoDBDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateMongoDBDatabaseParameters** | [**MongoDBDatabaseCreateUpdateParameters**](MongoDBDatabaseCreateUpdateParameters.md)| The parameters to provide for the current MongoDB database. | |

### Return type

[**MongoDBDatabaseGetResults**](MongoDBDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB database create or update operation was completed successfully. |  -  |
| **202** | The MongoDB database create or update operation will complete asynchronously. |  -  |

<a id="mongoDBResourcesDeleteMongoDBCollection"></a>
# **mongoDBResourcesDeleteMongoDBCollection**
> mongoDBResourcesDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Deletes an existing Azure Cosmos DB MongoDB Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String collectionName = "collectionName_example"; // String | Cosmos DB collection name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.mongoDBResourcesDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesDeleteMongoDBCollection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **collectionName** | **String**| Cosmos DB collection name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The MongoDB collection delete operation will complete asynchronously. |  -  |
| **204** | The MongoDB collection delete operation was completed successfully. |  -  |

<a id="mongoDBResourcesDeleteMongoDBDatabase"></a>
# **mongoDBResourcesDeleteMongoDBDatabase**
> mongoDBResourcesDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB MongoDB database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.mongoDBResourcesDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesDeleteMongoDBDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The MongoDB database delete operation will complete asynchronously. |  -  |
| **204** | The MongoDB database delete operation was completed successfully. |  -  |

<a id="mongoDBResourcesGetMongoDBCollection"></a>
# **mongoDBResourcesGetMongoDBCollection**
> MongoDBCollectionGetResults mongoDBResourcesGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Gets the MongoDB collection under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String collectionName = "collectionName_example"; // String | Cosmos DB collection name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MongoDBCollectionGetResults result = apiInstance.mongoDBResourcesGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesGetMongoDBCollection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **collectionName** | **String**| Cosmos DB collection name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MongoDBCollectionGetResults**](MongoDBCollectionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB collection property was retrieved successfully. |  -  |

<a id="mongoDBResourcesGetMongoDBCollectionThroughput"></a>
# **mongoDBResourcesGetMongoDBCollectionThroughput**
> ThroughputSettingsGetResults mongoDBResourcesGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



Gets the RUs per second of the MongoDB collection under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String collectionName = "collectionName_example"; // String | Cosmos DB collection name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.mongoDBResourcesGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesGetMongoDBCollectionThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **collectionName** | **String**| Cosmos DB collection name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB collection was retrieved successfully. |  -  |

<a id="mongoDBResourcesGetMongoDBDatabase"></a>
# **mongoDBResourcesGetMongoDBDatabase**
> MongoDBDatabaseGetResults mongoDBResourcesGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the MongoDB databases under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MongoDBDatabaseGetResults result = apiInstance.mongoDBResourcesGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesGetMongoDBDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MongoDBDatabaseGetResults**](MongoDBDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB database property was retrieved successfully. |  -  |

<a id="mongoDBResourcesGetMongoDBDatabaseThroughput"></a>
# **mongoDBResourcesGetMongoDBDatabaseThroughput**
> ThroughputSettingsGetResults mongoDBResourcesGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the MongoDB database under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.mongoDBResourcesGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesGetMongoDBDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB database was retrieved successfully. |  -  |

<a id="mongoDBResourcesListMongoDBCollections"></a>
# **mongoDBResourcesListMongoDBCollections**
> MongoDBCollectionListResult mongoDBResourcesListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the MongoDB collection under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MongoDBCollectionListResult result = apiInstance.mongoDBResourcesListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesListMongoDBCollections");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MongoDBCollectionListResult**](MongoDBCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB collection properties were retrieved successfully. |  -  |

<a id="mongoDBResourcesListMongoDBDatabases"></a>
# **mongoDBResourcesListMongoDBDatabases**
> MongoDBDatabaseListResult mongoDBResourcesListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the MongoDB databases under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      MongoDBDatabaseListResult result = apiInstance.mongoDBResourcesListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesListMongoDBDatabases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**MongoDBDatabaseListResult**](MongoDBDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB database properties were retrieved successfully. |  -  |

<a id="mongoDBResourcesUpdateMongoDBCollectionThroughput"></a>
# **mongoDBResourcesUpdateMongoDBCollectionThroughput**
> ThroughputSettingsGetResults mongoDBResourcesUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters)



Update the RUs per second of an Azure Cosmos DB MongoDB collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String collectionName = "collectionName_example"; // String | Cosmos DB collection name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB collection.
    try {
      ThroughputSettingsGetResults result = apiInstance.mongoDBResourcesUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesUpdateMongoDBCollectionThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **collectionName** | **String**| Cosmos DB collection name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB collection. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB collection update operation was completed successfully. |  -  |
| **202** | The RUs per second of the MongoDB collection update operation will complete asynchronously. |  -  |

<a id="mongoDBResourcesUpdateMongoDBDatabaseThroughput"></a>
# **mongoDBResourcesUpdateMongoDBDatabaseThroughput**
> ThroughputSettingsGetResults mongoDBResourcesUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of the an Azure Cosmos DB MongoDB database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB database.
    try {
      ThroughputSettingsGetResults result = apiInstance.mongoDBResourcesUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mongoDBResourcesUpdateMongoDBDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB database. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB database update operation was completed successfully. |  -  |
| **202** | The RUs per second of the MongoDB database update operation will complete asynchronously. |  -  |

<a id="partitionKeyRangeIdListMetrics"></a>
# **partitionKeyRangeIdListMetrics**
> PartitionMetricListResult partitionKeyRangeIdListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given partition key range id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String partitionKeyRangeId = "partitionKeyRangeId_example"; // String | Partition Key Range Id for which to get data.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PartitionMetricListResult result = apiInstance.partitionKeyRangeIdListMetrics(subscriptionId, resourceGroupName, accountName, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionKeyRangeIdListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **partitionKeyRangeId** | **String**| Partition Key Range Id for which to get data. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition-level metrics for the partition key range id were retrieved successfully. |  -  |

<a id="partitionKeyRangeIdRegionListMetrics"></a>
# **partitionKeyRangeIdRegionListMetrics**
> PartitionMetricListResult partitionKeyRangeIdRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given partition key range id and region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String region = "region_example"; // String | Cosmos DB region, with spaces between words and each word capitalized.
    String databaseRid = "databaseRid_example"; // String | Cosmos DB database rid.
    String collectionRid = "collectionRid_example"; // String | Cosmos DB collection rid.
    String partitionKeyRangeId = "partitionKeyRangeId_example"; // String | Partition Key Range Id for which to get data.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PartitionMetricListResult result = apiInstance.partitionKeyRangeIdRegionListMetrics(subscriptionId, resourceGroupName, accountName, region, databaseRid, collectionRid, partitionKeyRangeId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionKeyRangeIdRegionListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **region** | **String**| Cosmos DB region, with spaces between words and each word capitalized. | |
| **databaseRid** | **String**| Cosmos DB database rid. | |
| **collectionRid** | **String**| Cosmos DB collection rid. | |
| **partitionKeyRangeId** | **String**| Partition Key Range Id for which to get data. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PartitionMetricListResult**](PartitionMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition-level metrics for the partition key range id and region were retrieved successfully. |  -  |

<a id="percentileListMetrics"></a>
# **percentileListMetrics**
> PercentileMetricListResult percentileListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given database account. This url is only for PBS and Replication Latency data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PercentileMetricListResult result = apiInstance.percentileListMetrics(subscriptionId, resourceGroupName, accountName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#percentileListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The percentile metrics for the account were retrieved successfully. |  -  |

<a id="percentileSourceTargetListMetrics"></a>
# **percentileSourceTargetListMetrics**
> PercentileMetricListResult percentileSourceTargetListMetrics(subscriptionId, resourceGroupName, accountName, sourceRegion, targetRegion, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given account, source and target region. This url is only for PBS and Replication Latency data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String sourceRegion = "sourceRegion_example"; // String | Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    String targetRegion = "targetRegion_example"; // String | Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PercentileMetricListResult result = apiInstance.percentileSourceTargetListMetrics(subscriptionId, resourceGroupName, accountName, sourceRegion, targetRegion, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#percentileSourceTargetListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **sourceRegion** | **String**| Source region from which data is written. Cosmos DB region, with spaces between words and each word capitalized. | |
| **targetRegion** | **String**| Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The percentile metrics for the account, source and target regions were retrieved successfully. |  -  |

<a id="percentileTargetListMetrics"></a>
# **percentileTargetListMetrics**
> PercentileMetricListResult percentileTargetListMetrics(subscriptionId, resourceGroupName, accountName, targetRegion, apiVersion, $filter)



Retrieves the metrics determined by the given filter for the given account target region. This url is only for PBS and Replication Latency data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String targetRegion = "targetRegion_example"; // String | Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String $filter = "$filter_example"; // String | An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq.
    try {
      PercentileMetricListResult result = apiInstance.percentileTargetListMetrics(subscriptionId, resourceGroupName, accountName, targetRegion, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#percentileTargetListMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **targetRegion** | **String**| Target region to which data is written. Cosmos DB region, with spaces between words and each word capitalized. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **$filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | |

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The percentile metrics for the account and target regions were retrieved successfully. |  -  |

<a id="sqlResourcesCreateUpdateSqlContainer"></a>
# **sqlResourcesCreateUpdateSqlContainer**
> SqlContainerGetResults sqlResourcesCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters)



Create or update an Azure Cosmos DB SQL container

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    SqlContainerCreateUpdateParameters createUpdateSqlContainerParameters = new SqlContainerCreateUpdateParameters(); // SqlContainerCreateUpdateParameters | The parameters to provide for the current SQL container.
    try {
      SqlContainerGetResults result = apiInstance.sqlResourcesCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesCreateUpdateSqlContainer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateSqlContainerParameters** | [**SqlContainerCreateUpdateParameters**](SqlContainerCreateUpdateParameters.md)| The parameters to provide for the current SQL container. | |

### Return type

[**SqlContainerGetResults**](SqlContainerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL container create or update operation was completed successfully. |  -  |
| **202** | The SQL container create or update operation will complete asynchronously. |  -  |

<a id="sqlResourcesCreateUpdateSqlDatabase"></a>
# **sqlResourcesCreateUpdateSqlDatabase**
> SqlDatabaseGetResults sqlResourcesCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters)



Create or update an Azure Cosmos DB SQL database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    SqlDatabaseCreateUpdateParameters createUpdateSqlDatabaseParameters = new SqlDatabaseCreateUpdateParameters(); // SqlDatabaseCreateUpdateParameters | The parameters to provide for the current SQL database.
    try {
      SqlDatabaseGetResults result = apiInstance.sqlResourcesCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesCreateUpdateSqlDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateSqlDatabaseParameters** | [**SqlDatabaseCreateUpdateParameters**](SqlDatabaseCreateUpdateParameters.md)| The parameters to provide for the current SQL database. | |

### Return type

[**SqlDatabaseGetResults**](SqlDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL database create or update operation was completed successfully. |  -  |
| **202** | The SQL database create or update operation will complete asynchronously. |  -  |

<a id="sqlResourcesCreateUpdateSqlStoredProcedure"></a>
# **sqlResourcesCreateUpdateSqlStoredProcedure**
> SqlStoredProcedureGetResults sqlResourcesCreateUpdateSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, createUpdateSqlStoredProcedureParameters)



Create or update an Azure Cosmos DB SQL storedProcedure

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    SqlStoredProcedureCreateUpdateParameters createUpdateSqlStoredProcedureParameters = new SqlStoredProcedureCreateUpdateParameters(); // SqlStoredProcedureCreateUpdateParameters | The parameters to provide for the current SQL storedProcedure.
    try {
      SqlStoredProcedureGetResults result = apiInstance.sqlResourcesCreateUpdateSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion, createUpdateSqlStoredProcedureParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesCreateUpdateSqlStoredProcedure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateSqlStoredProcedureParameters** | [**SqlStoredProcedureCreateUpdateParameters**](SqlStoredProcedureCreateUpdateParameters.md)| The parameters to provide for the current SQL storedProcedure. | |

### Return type

[**SqlStoredProcedureGetResults**](SqlStoredProcedureGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL storedProcedure create or update operation was completed successfully. |  -  |
| **202** | The SQL storedProcedure create or update operation will complete asynchronously. |  -  |

<a id="sqlResourcesCreateUpdateSqlTrigger"></a>
# **sqlResourcesCreateUpdateSqlTrigger**
> SqlTriggerGetResults sqlResourcesCreateUpdateSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, createUpdateSqlTriggerParameters)



Create or update an Azure Cosmos DB SQL trigger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    SqlTriggerCreateUpdateParameters createUpdateSqlTriggerParameters = new SqlTriggerCreateUpdateParameters(); // SqlTriggerCreateUpdateParameters | The parameters to provide for the current SQL trigger.
    try {
      SqlTriggerGetResults result = apiInstance.sqlResourcesCreateUpdateSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion, createUpdateSqlTriggerParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesCreateUpdateSqlTrigger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **triggerName** | **String**| Cosmos DB trigger name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateSqlTriggerParameters** | [**SqlTriggerCreateUpdateParameters**](SqlTriggerCreateUpdateParameters.md)| The parameters to provide for the current SQL trigger. | |

### Return type

[**SqlTriggerGetResults**](SqlTriggerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL trigger create or update operation was completed successfully. |  -  |
| **202** | The SQL trigger create or update operation will complete asynchronously. |  -  |

<a id="sqlResourcesCreateUpdateSqlUserDefinedFunction"></a>
# **sqlResourcesCreateUpdateSqlUserDefinedFunction**
> SqlUserDefinedFunctionGetResults sqlResourcesCreateUpdateSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, createUpdateSqlUserDefinedFunctionParameters)



Create or update an Azure Cosmos DB SQL userDefinedFunction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    SqlUserDefinedFunctionCreateUpdateParameters createUpdateSqlUserDefinedFunctionParameters = new SqlUserDefinedFunctionCreateUpdateParameters(); // SqlUserDefinedFunctionCreateUpdateParameters | The parameters to provide for the current SQL userDefinedFunction.
    try {
      SqlUserDefinedFunctionGetResults result = apiInstance.sqlResourcesCreateUpdateSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion, createUpdateSqlUserDefinedFunctionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesCreateUpdateSqlUserDefinedFunction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateSqlUserDefinedFunctionParameters** | [**SqlUserDefinedFunctionCreateUpdateParameters**](SqlUserDefinedFunctionCreateUpdateParameters.md)| The parameters to provide for the current SQL userDefinedFunction. | |

### Return type

[**SqlUserDefinedFunctionGetResults**](SqlUserDefinedFunctionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL userDefinedFunction create or update operation was completed successfully. |  -  |
| **202** | The SQL userDefinedFunction create or update operation will complete asynchronously. |  -  |

<a id="sqlResourcesDeleteSqlContainer"></a>
# **sqlResourcesDeleteSqlContainer**
> sqlResourcesDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Deletes an existing Azure Cosmos DB SQL container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.sqlResourcesDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesDeleteSqlContainer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The SQL container delete operation will complete asynchronously. |  -  |
| **204** | The SQL container delete operation was completed successfully. |  -  |

<a id="sqlResourcesDeleteSqlDatabase"></a>
# **sqlResourcesDeleteSqlDatabase**
> sqlResourcesDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Deletes an existing Azure Cosmos DB SQL database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.sqlResourcesDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesDeleteSqlDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The SQL database delete operation will complete asynchronously. |  -  |
| **204** | The SQL database delete operation was completed successfully. |  -  |

<a id="sqlResourcesDeleteSqlStoredProcedure"></a>
# **sqlResourcesDeleteSqlStoredProcedure**
> sqlResourcesDeleteSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion)



Deletes an existing Azure Cosmos DB SQL storedProcedure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.sqlResourcesDeleteSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesDeleteSqlStoredProcedure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The SQL storedProcedure delete operation will complete asynchronously. |  -  |
| **204** | The SQL storedProcedure delete operation was completed successfully. |  -  |

<a id="sqlResourcesDeleteSqlTrigger"></a>
# **sqlResourcesDeleteSqlTrigger**
> sqlResourcesDeleteSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion)



Deletes an existing Azure Cosmos DB SQL trigger.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.sqlResourcesDeleteSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesDeleteSqlTrigger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **triggerName** | **String**| Cosmos DB trigger name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The SQL trigger delete operation will complete asynchronously. |  -  |
| **204** | The SQL trigger delete operation was completed successfully. |  -  |

<a id="sqlResourcesDeleteSqlUserDefinedFunction"></a>
# **sqlResourcesDeleteSqlUserDefinedFunction**
> sqlResourcesDeleteSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion)



Deletes an existing Azure Cosmos DB SQL userDefinedFunction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.sqlResourcesDeleteSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesDeleteSqlUserDefinedFunction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The SQL userDefinedFunction delete operation will complete asynchronously. |  -  |
| **204** | The SQL userDefinedFunction delete operation was completed successfully. |  -  |

<a id="sqlResourcesGetSqlContainer"></a>
# **sqlResourcesGetSqlContainer**
> SqlContainerGetResults sqlResourcesGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Gets the SQL container under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlContainerGetResults result = apiInstance.sqlResourcesGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlContainer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlContainerGetResults**](SqlContainerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL container property was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlContainerThroughput"></a>
# **sqlResourcesGetSqlContainerThroughput**
> ThroughputSettingsGetResults sqlResourcesGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Gets the RUs per second of the SQL container under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.sqlResourcesGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlContainerThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL container was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlDatabase"></a>
# **sqlResourcesGetSqlDatabase**
> SqlDatabaseGetResults sqlResourcesGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the SQL database under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlDatabaseGetResults result = apiInstance.sqlResourcesGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlDatabase");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlDatabaseGetResults**](SqlDatabaseGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL database property was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlDatabaseThroughput"></a>
# **sqlResourcesGetSqlDatabaseThroughput**
> ThroughputSettingsGetResults sqlResourcesGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Gets the RUs per second of the SQL database under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.sqlResourcesGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL database was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlStoredProcedure"></a>
# **sqlResourcesGetSqlStoredProcedure**
> SqlStoredProcedureGetResults sqlResourcesGetSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion)



Gets the SQL storedProcedure under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String storedProcedureName = "storedProcedureName_example"; // String | Cosmos DB storedProcedure name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlStoredProcedureGetResults result = apiInstance.sqlResourcesGetSqlStoredProcedure(subscriptionId, resourceGroupName, accountName, databaseName, containerName, storedProcedureName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlStoredProcedure");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **storedProcedureName** | **String**| Cosmos DB storedProcedure name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlStoredProcedureGetResults**](SqlStoredProcedureGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL storedProcedure property was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlTrigger"></a>
# **sqlResourcesGetSqlTrigger**
> SqlTriggerGetResults sqlResourcesGetSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion)



Gets the SQL trigger under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String triggerName = "triggerName_example"; // String | Cosmos DB trigger name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlTriggerGetResults result = apiInstance.sqlResourcesGetSqlTrigger(subscriptionId, resourceGroupName, accountName, databaseName, containerName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlTrigger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **triggerName** | **String**| Cosmos DB trigger name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlTriggerGetResults**](SqlTriggerGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL trigger property was retrieved successfully. |  -  |

<a id="sqlResourcesGetSqlUserDefinedFunction"></a>
# **sqlResourcesGetSqlUserDefinedFunction**
> SqlUserDefinedFunctionGetResults sqlResourcesGetSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion)



Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String userDefinedFunctionName = "userDefinedFunctionName_example"; // String | Cosmos DB userDefinedFunction name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlUserDefinedFunctionGetResults result = apiInstance.sqlResourcesGetSqlUserDefinedFunction(subscriptionId, resourceGroupName, accountName, databaseName, containerName, userDefinedFunctionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesGetSqlUserDefinedFunction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **userDefinedFunctionName** | **String**| Cosmos DB userDefinedFunction name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlUserDefinedFunctionGetResults**](SqlUserDefinedFunctionGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL userDefinedFunction property was retrieved successfully. |  -  |

<a id="sqlResourcesListSqlContainers"></a>
# **sqlResourcesListSqlContainers**
> SqlContainerListResult sqlResourcesListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



Lists the SQL container under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlContainerListResult result = apiInstance.sqlResourcesListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesListSqlContainers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlContainerListResult**](SqlContainerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL container properties were retrieved successfully. |  -  |

<a id="sqlResourcesListSqlDatabases"></a>
# **sqlResourcesListSqlDatabases**
> SqlDatabaseListResult sqlResourcesListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the SQL databases under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlDatabaseListResult result = apiInstance.sqlResourcesListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesListSqlDatabases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlDatabaseListResult**](SqlDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL database properties were retrieved successfully. |  -  |

<a id="sqlResourcesListSqlStoredProcedures"></a>
# **sqlResourcesListSqlStoredProcedures**
> SqlStoredProcedureListResult sqlResourcesListSqlStoredProcedures(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlStoredProcedureListResult result = apiInstance.sqlResourcesListSqlStoredProcedures(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesListSqlStoredProcedures");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlStoredProcedureListResult**](SqlStoredProcedureListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL stored procedure properties were retrieved successfully. |  -  |

<a id="sqlResourcesListSqlTriggers"></a>
# **sqlResourcesListSqlTriggers**
> SqlTriggerListResult sqlResourcesListSqlTriggers(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL trigger under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlTriggerListResult result = apiInstance.sqlResourcesListSqlTriggers(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesListSqlTriggers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlTriggerListResult**](SqlTriggerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL trigger properties were retrieved successfully. |  -  |

<a id="sqlResourcesListSqlUserDefinedFunctions"></a>
# **sqlResourcesListSqlUserDefinedFunctions**
> SqlUserDefinedFunctionListResult sqlResourcesListSqlUserDefinedFunctions(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



Lists the SQL userDefinedFunction under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      SqlUserDefinedFunctionListResult result = apiInstance.sqlResourcesListSqlUserDefinedFunctions(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesListSqlUserDefinedFunctions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**SqlUserDefinedFunctionListResult**](SqlUserDefinedFunctionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL userDefinedFunction properties were retrieved successfully. |  -  |

<a id="sqlResourcesUpdateSqlContainerThroughput"></a>
# **sqlResourcesUpdateSqlContainerThroughput**
> ThroughputSettingsGetResults sqlResourcesUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB SQL container

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String containerName = "containerName_example"; // String | Cosmos DB container name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current SQL container.
    try {
      ThroughputSettingsGetResults result = apiInstance.sqlResourcesUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesUpdateSqlContainerThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **containerName** | **String**| Cosmos DB container name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL container. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL container update operation was completed successfully. |  -  |
| **202** | The RUs per second of the SQL container update operation will complete asynchronously. |  -  |

<a id="sqlResourcesUpdateSqlDatabaseThroughput"></a>
# **sqlResourcesUpdateSqlDatabaseThroughput**
> ThroughputSettingsGetResults sqlResourcesUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB SQL database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String databaseName = "databaseName_example"; // String | Cosmos DB database name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current SQL database.
    try {
      ThroughputSettingsGetResults result = apiInstance.sqlResourcesUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sqlResourcesUpdateSqlDatabaseThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **databaseName** | **String**| Cosmos DB database name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL database. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL database update operation was completed successfully. |  -  |
| **202** | The RUs per second of the SQL database update operation will complete asynchronously. |  -  |

<a id="tableResourcesCreateUpdateTable"></a>
# **tableResourcesCreateUpdateTable**
> TableGetResults tableResourcesCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters)



Create or update an Azure Cosmos DB Table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    TableCreateUpdateParameters createUpdateTableParameters = new TableCreateUpdateParameters(); // TableCreateUpdateParameters | The parameters to provide for the current Table.
    try {
      TableGetResults result = apiInstance.tableResourcesCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesCreateUpdateTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **createUpdateTableParameters** | [**TableCreateUpdateParameters**](TableCreateUpdateParameters.md)| The parameters to provide for the current Table. | |

### Return type

[**TableGetResults**](TableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Table create or update operation was completed successfully. |  -  |
| **202** | The Table create or update operation will complete asynchronously. |  -  |

<a id="tableResourcesDeleteTable"></a>
# **tableResourcesDeleteTable**
> tableResourcesDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Deletes an existing Azure Cosmos DB Table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      apiInstance.tableResourcesDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesDeleteTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The Table delete operation will complete asynchronously. |  -  |
| **204** | The Table delete operation was completed successfully. |  -  |

<a id="tableResourcesGetTable"></a>
# **tableResourcesGetTable**
> TableGetResults tableResourcesGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Gets the Tables under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      TableGetResults result = apiInstance.tableResourcesGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesGetTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**TableGetResults**](TableGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Table property was retrieved successfully. |  -  |

<a id="tableResourcesGetTableThroughput"></a>
# **tableResourcesGetTableThroughput**
> ThroughputSettingsGetResults tableResourcesGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



Gets the RUs per second of the Table under an existing Azure Cosmos DB database account with the provided name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      ThroughputSettingsGetResults result = apiInstance.tableResourcesGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesGetTableThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Table was retrieved successfully. |  -  |

<a id="tableResourcesListTables"></a>
# **tableResourcesListTables**
> TableListResult tableResourcesListTables(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Tables under an existing Azure Cosmos DB database account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    try {
      TableListResult result = apiInstance.tableResourcesListTables(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesListTables");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |

### Return type

[**TableListResult**](TableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Table properties were retrieved successfully. |  -  |

<a id="tableResourcesUpdateTableThroughput"></a>
# **tableResourcesUpdateTableThroughput**
> ThroughputSettingsGetResults tableResourcesUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters)



Update RUs per second of an Azure Cosmos DB Table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String tableName = "tableName_example"; // String | Cosmos DB table name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    ThroughputSettingsUpdateParameters updateThroughputParameters = new ThroughputSettingsUpdateParameters(); // ThroughputSettingsUpdateParameters | The parameters to provide for the RUs per second of the current Table.
    try {
      ThroughputSettingsGetResults result = apiInstance.tableResourcesUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tableResourcesUpdateTableThroughput");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **tableName** | **String**| Cosmos DB table name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **updateThroughputParameters** | [**ThroughputSettingsUpdateParameters**](ThroughputSettingsUpdateParameters.md)| The parameters to provide for the RUs per second of the current Table. | |

### Return type

[**ThroughputSettingsGetResults**](ThroughputSettingsGetResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Table update operation was completed successfully. |  -  |
| **202** | The RUs per second of the Table update operation will complete asynchronously. |  -  |

