# CosmosDb.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
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
[**databaseAccountsCreateUpdateCassandraKeyspace**](DefaultApi.md#databaseAccountsCreateUpdateCassandraKeyspace) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} | 
[**databaseAccountsCreateUpdateCassandraTable**](DefaultApi.md#databaseAccountsCreateUpdateCassandraTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} | 
[**databaseAccountsCreateUpdateGremlinDatabase**](DefaultApi.md#databaseAccountsCreateUpdateGremlinDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} | 
[**databaseAccountsCreateUpdateGremlinGraph**](DefaultApi.md#databaseAccountsCreateUpdateGremlinGraph) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} | 
[**databaseAccountsCreateUpdateMongoDBCollection**](DefaultApi.md#databaseAccountsCreateUpdateMongoDBCollection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} | 
[**databaseAccountsCreateUpdateMongoDBDatabase**](DefaultApi.md#databaseAccountsCreateUpdateMongoDBDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} | 
[**databaseAccountsCreateUpdateSqlContainer**](DefaultApi.md#databaseAccountsCreateUpdateSqlContainer) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} | 
[**databaseAccountsCreateUpdateSqlDatabase**](DefaultApi.md#databaseAccountsCreateUpdateSqlDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} | 
[**databaseAccountsCreateUpdateTable**](DefaultApi.md#databaseAccountsCreateUpdateTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} | 
[**databaseAccountsDelete**](DefaultApi.md#databaseAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsDeleteCassandraKeyspace**](DefaultApi.md#databaseAccountsDeleteCassandraKeyspace) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} | 
[**databaseAccountsDeleteCassandraTable**](DefaultApi.md#databaseAccountsDeleteCassandraTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} | 
[**databaseAccountsDeleteGremlinDatabase**](DefaultApi.md#databaseAccountsDeleteGremlinDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} | 
[**databaseAccountsDeleteGremlinGraph**](DefaultApi.md#databaseAccountsDeleteGremlinGraph) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} | 
[**databaseAccountsDeleteMongoDBCollection**](DefaultApi.md#databaseAccountsDeleteMongoDBCollection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} | 
[**databaseAccountsDeleteMongoDBDatabase**](DefaultApi.md#databaseAccountsDeleteMongoDBDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} | 
[**databaseAccountsDeleteSqlContainer**](DefaultApi.md#databaseAccountsDeleteSqlContainer) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} | 
[**databaseAccountsDeleteSqlDatabase**](DefaultApi.md#databaseAccountsDeleteSqlDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} | 
[**databaseAccountsDeleteTable**](DefaultApi.md#databaseAccountsDeleteTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} | 
[**databaseAccountsFailoverPriorityChange**](DefaultApi.md#databaseAccountsFailoverPriorityChange) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/failoverPriorityChange | 
[**databaseAccountsGet**](DefaultApi.md#databaseAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsGetCassandraKeyspace**](DefaultApi.md#databaseAccountsGetCassandraKeyspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} | 
[**databaseAccountsGetCassandraKeyspaceThroughput**](DefaultApi.md#databaseAccountsGetCassandraKeyspaceThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/settings/throughput | 
[**databaseAccountsGetCassandraTable**](DefaultApi.md#databaseAccountsGetCassandraTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} | 
[**databaseAccountsGetCassandraTableThroughput**](DefaultApi.md#databaseAccountsGetCassandraTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName}/settings/throughput | 
[**databaseAccountsGetGremlinDatabase**](DefaultApi.md#databaseAccountsGetGremlinDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} | 
[**databaseAccountsGetGremlinDatabaseThroughput**](DefaultApi.md#databaseAccountsGetGremlinDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/settings/throughput | 
[**databaseAccountsGetGremlinGraph**](DefaultApi.md#databaseAccountsGetGremlinGraph) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} | 
[**databaseAccountsGetGremlinGraphThroughput**](DefaultApi.md#databaseAccountsGetGremlinGraphThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName}/settings/throughput | 
[**databaseAccountsGetMongoDBCollection**](DefaultApi.md#databaseAccountsGetMongoDBCollection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} | 
[**databaseAccountsGetMongoDBCollectionThroughput**](DefaultApi.md#databaseAccountsGetMongoDBCollectionThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName}/settings/throughput | 
[**databaseAccountsGetMongoDBDatabase**](DefaultApi.md#databaseAccountsGetMongoDBDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} | 
[**databaseAccountsGetMongoDBDatabaseThroughput**](DefaultApi.md#databaseAccountsGetMongoDBDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/settings/throughput | 
[**databaseAccountsGetReadOnlyKeys**](DefaultApi.md#databaseAccountsGetReadOnlyKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys | 
[**databaseAccountsGetSqlContainer**](DefaultApi.md#databaseAccountsGetSqlContainer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} | 
[**databaseAccountsGetSqlContainerThroughput**](DefaultApi.md#databaseAccountsGetSqlContainerThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName}/settings/throughput | 
[**databaseAccountsGetSqlDatabase**](DefaultApi.md#databaseAccountsGetSqlDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} | 
[**databaseAccountsGetSqlDatabaseThroughput**](DefaultApi.md#databaseAccountsGetSqlDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/settings/throughput | 
[**databaseAccountsGetTable**](DefaultApi.md#databaseAccountsGetTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} | 
[**databaseAccountsGetTableThroughput**](DefaultApi.md#databaseAccountsGetTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName}/settings/throughput | 
[**databaseAccountsList**](DefaultApi.md#databaseAccountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/databaseAccounts | 
[**databaseAccountsListByResourceGroup**](DefaultApi.md#databaseAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts | 
[**databaseAccountsListCassandraKeyspaces**](DefaultApi.md#databaseAccountsListCassandraKeyspaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces | 
[**databaseAccountsListCassandraTables**](DefaultApi.md#databaseAccountsListCassandraTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables | 
[**databaseAccountsListConnectionStrings**](DefaultApi.md#databaseAccountsListConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listConnectionStrings | 
[**databaseAccountsListGremlinDatabases**](DefaultApi.md#databaseAccountsListGremlinDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases | 
[**databaseAccountsListGremlinGraphs**](DefaultApi.md#databaseAccountsListGremlinGraphs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs | 
[**databaseAccountsListKeys**](DefaultApi.md#databaseAccountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listKeys | 
[**databaseAccountsListMetricDefinitions**](DefaultApi.md#databaseAccountsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metricDefinitions | 
[**databaseAccountsListMetrics**](DefaultApi.md#databaseAccountsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metrics | 
[**databaseAccountsListMongoDBCollections**](DefaultApi.md#databaseAccountsListMongoDBCollections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections | 
[**databaseAccountsListMongoDBDatabases**](DefaultApi.md#databaseAccountsListMongoDBDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases | 
[**databaseAccountsListReadOnlyKeys**](DefaultApi.md#databaseAccountsListReadOnlyKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys | 
[**databaseAccountsListSqlContainers**](DefaultApi.md#databaseAccountsListSqlContainers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers | 
[**databaseAccountsListSqlDatabases**](DefaultApi.md#databaseAccountsListSqlDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases | 
[**databaseAccountsListTables**](DefaultApi.md#databaseAccountsListTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables | 
[**databaseAccountsListUsages**](DefaultApi.md#databaseAccountsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/usages | 
[**databaseAccountsOfflineRegion**](DefaultApi.md#databaseAccountsOfflineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/offlineRegion | 
[**databaseAccountsOnlineRegion**](DefaultApi.md#databaseAccountsOnlineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/onlineRegion | 
[**databaseAccountsPatch**](DefaultApi.md#databaseAccountsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} | 
[**databaseAccountsRegenerateKey**](DefaultApi.md#databaseAccountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/regenerateKey | 
[**databaseAccountsUpdateCassandraKeyspaceThroughput**](DefaultApi.md#databaseAccountsUpdateCassandraKeyspaceThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/settings/throughput | 
[**databaseAccountsUpdateCassandraTableThroughput**](DefaultApi.md#databaseAccountsUpdateCassandraTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName}/settings/throughput | 
[**databaseAccountsUpdateGremlinDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateGremlinDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/settings/throughput | 
[**databaseAccountsUpdateGremlinGraphThroughput**](DefaultApi.md#databaseAccountsUpdateGremlinGraphThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName}/settings/throughput | 
[**databaseAccountsUpdateMongoDBCollectionThroughput**](DefaultApi.md#databaseAccountsUpdateMongoDBCollectionThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName}/settings/throughput | 
[**databaseAccountsUpdateMongoDBDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateMongoDBDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/settings/throughput | 
[**databaseAccountsUpdateSqlContainerThroughput**](DefaultApi.md#databaseAccountsUpdateSqlContainerThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName}/settings/throughput | 
[**databaseAccountsUpdateSqlDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateSqlDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/settings/throughput | 
[**databaseAccountsUpdateTableThroughput**](DefaultApi.md#databaseAccountsUpdateTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName}/settings/throughput | 
[**databaseListMetricDefinitions**](DefaultApi.md#databaseListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metricDefinitions | 
[**databaseListMetrics**](DefaultApi.md#databaseListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metrics | 
[**databaseListUsages**](DefaultApi.md#databaseListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/usages | 
[**partitionKeyRangeIdListMetrics**](DefaultApi.md#partitionKeyRangeIdListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics | 
[**partitionKeyRangeIdRegionListMetrics**](DefaultApi.md#partitionKeyRangeIdRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics | 
[**percentileListMetrics**](DefaultApi.md#percentileListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/percentile/metrics | 
[**percentileSourceTargetListMetrics**](DefaultApi.md#percentileSourceTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sourceRegion/{sourceRegion}/targetRegion/{targetRegion}/percentile/metrics | 
[**percentileTargetListMetrics**](DefaultApi.md#percentileTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/targetRegion/{targetRegion}/percentile/metrics | 



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsCreateOrUpdate

> DatabaseAccount databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters)



Creates or updates an Azure Cosmos DB database account.

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateParameters** | [**DatabaseAccountCreateUpdateParameters**](DatabaseAccountCreateUpdateParameters.md)| The parameters to provide for the current database account. | 

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateCassandraKeyspace

> CassandraKeyspace databaseAccountsCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateCassandraKeyspaceParameters = new CosmosDb.CassandraKeyspaceCreateUpdateParameters(); // CassandraKeyspaceCreateUpdateParameters | The parameters to provide for the current Cassandra keyspace.
apiInstance.databaseAccountsCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateCassandraKeyspaceParameters** | [**CassandraKeyspaceCreateUpdateParameters**](CassandraKeyspaceCreateUpdateParameters.md)| The parameters to provide for the current Cassandra keyspace. | 

### Return type

[**CassandraKeyspace**](CassandraKeyspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateCassandraTable

> CassandraTable databaseAccountsCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateCassandraTableParameters = new CosmosDb.CassandraTableCreateUpdateParameters(); // CassandraTableCreateUpdateParameters | The parameters to provide for the current Cassandra Table.
apiInstance.databaseAccountsCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateCassandraTableParameters** | [**CassandraTableCreateUpdateParameters**](CassandraTableCreateUpdateParameters.md)| The parameters to provide for the current Cassandra Table. | 

### Return type

[**CassandraTable**](CassandraTable.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateGremlinDatabase

> GremlinDatabase databaseAccountsCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateGremlinDatabaseParameters = new CosmosDb.GremlinDatabaseCreateUpdateParameters(); // GremlinDatabaseCreateUpdateParameters | The parameters to provide for the current Gremlin database.
apiInstance.databaseAccountsCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateGremlinDatabaseParameters** | [**GremlinDatabaseCreateUpdateParameters**](GremlinDatabaseCreateUpdateParameters.md)| The parameters to provide for the current Gremlin database. | 

### Return type

[**GremlinDatabase**](GremlinDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateGremlinGraph

> GremlinGraph databaseAccountsCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateGremlinGraphParameters = new CosmosDb.GremlinGraphCreateUpdateParameters(); // GremlinGraphCreateUpdateParameters | The parameters to provide for the current Gremlin graph.
apiInstance.databaseAccountsCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateGremlinGraphParameters** | [**GremlinGraphCreateUpdateParameters**](GremlinGraphCreateUpdateParameters.md)| The parameters to provide for the current Gremlin graph. | 

### Return type

[**GremlinGraph**](GremlinGraph.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateMongoDBCollection

> MongoDBCollection databaseAccountsCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateMongoDBCollectionParameters = new CosmosDb.MongoDBCollectionCreateUpdateParameters(); // MongoDBCollectionCreateUpdateParameters | The parameters to provide for the current MongoDB Collection.
apiInstance.databaseAccountsCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateMongoDBCollectionParameters** | [**MongoDBCollectionCreateUpdateParameters**](MongoDBCollectionCreateUpdateParameters.md)| The parameters to provide for the current MongoDB Collection. | 

### Return type

[**MongoDBCollection**](MongoDBCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateMongoDBDatabase

> MongoDBDatabase databaseAccountsCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateMongoDBDatabaseParameters = new CosmosDb.MongoDBDatabaseCreateUpdateParameters(); // MongoDBDatabaseCreateUpdateParameters | The parameters to provide for the current MongoDB database.
apiInstance.databaseAccountsCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateMongoDBDatabaseParameters** | [**MongoDBDatabaseCreateUpdateParameters**](MongoDBDatabaseCreateUpdateParameters.md)| The parameters to provide for the current MongoDB database. | 

### Return type

[**MongoDBDatabase**](MongoDBDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateSqlContainer

> SqlContainer databaseAccountsCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateSqlContainerParameters = new CosmosDb.SqlContainerCreateUpdateParameters(); // SqlContainerCreateUpdateParameters | The parameters to provide for the current SQL container.
apiInstance.databaseAccountsCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateSqlContainerParameters** | [**SqlContainerCreateUpdateParameters**](SqlContainerCreateUpdateParameters.md)| The parameters to provide for the current SQL container. | 

### Return type

[**SqlContainer**](SqlContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateSqlDatabase

> SqlDatabase databaseAccountsCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateSqlDatabaseParameters = new CosmosDb.SqlDatabaseCreateUpdateParameters(); // SqlDatabaseCreateUpdateParameters | The parameters to provide for the current SQL database.
apiInstance.databaseAccountsCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateSqlDatabaseParameters** | [**SqlDatabaseCreateUpdateParameters**](SqlDatabaseCreateUpdateParameters.md)| The parameters to provide for the current SQL database. | 

### Return type

[**SqlDatabase**](SqlDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsCreateUpdateTable

> Table databaseAccountsCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let createUpdateTableParameters = new CosmosDb.TableCreateUpdateParameters(); // TableCreateUpdateParameters | The parameters to provide for the current Table.
apiInstance.databaseAccountsCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **createUpdateTableParameters** | [**TableCreateUpdateParameters**](TableCreateUpdateParameters.md)| The parameters to provide for the current Table. | 

### Return type

[**Table**](Table.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteCassandraKeyspace

> databaseAccountsDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteCassandraTable

> databaseAccountsDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteGremlinDatabase

> databaseAccountsDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteGremlinGraph

> databaseAccountsDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteMongoDBCollection

> databaseAccountsDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteMongoDBDatabase

> databaseAccountsDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteSqlContainer

> databaseAccountsDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteSqlDatabase

> databaseAccountsDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## databaseAccountsDeleteTable

> databaseAccountsDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **failoverParameters** | [**FailoverPolicies**](FailoverPolicies.md)| The new failover policies for the database account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## databaseAccountsGet

> DatabaseAccount databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetCassandraKeyspace

> CassandraKeyspace databaseAccountsGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**CassandraKeyspace**](CassandraKeyspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetCassandraKeyspaceThroughput

> Throughput databaseAccountsGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetCassandraTable

> CassandraTable databaseAccountsGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**CassandraTable**](CassandraTable.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetCassandraTableThroughput

> Throughput databaseAccountsGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetGremlinDatabase

> GremlinDatabase databaseAccountsGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**GremlinDatabase**](GremlinDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetGremlinDatabaseThroughput

> Throughput databaseAccountsGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetGremlinGraph

> GremlinGraph databaseAccountsGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**GremlinGraph**](GremlinGraph.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetGremlinGraphThroughput

> Throughput databaseAccountsGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetMongoDBCollection

> MongoDBCollection databaseAccountsGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**MongoDBCollection**](MongoDBCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetMongoDBCollectionThroughput

> Throughput databaseAccountsGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetMongoDBDatabase

> MongoDBDatabase databaseAccountsGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**MongoDBDatabase**](MongoDBDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetMongoDBDatabaseThroughput

> Throughput databaseAccountsGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetSqlContainer

> SqlContainer databaseAccountsGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**SqlContainer**](SqlContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetSqlContainerThroughput

> Throughput databaseAccountsGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetSqlDatabase

> SqlDatabase databaseAccountsGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**SqlDatabase**](SqlDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetSqlDatabaseThroughput

> Throughput databaseAccountsGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetTable

> Table databaseAccountsGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Table**](Table.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsGetTableThroughput

> Throughput databaseAccountsGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**Throughput**](Throughput.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **subscriptionId** | **String**| Azure subscription ID. | 

### Return type

[**DatabaseAccountsListResult**](DatabaseAccountsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListCassandraKeyspaces

> CassandraKeyspaceListResult databaseAccountsListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**CassandraKeyspaceListResult**](CassandraKeyspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListCassandraTables

> CassandraTableListResult databaseAccountsListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**CassandraTableListResult**](CassandraTableListResult.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**DatabaseAccountListConnectionStringsResult**](DatabaseAccountListConnectionStringsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListGremlinDatabases

> GremlinDatabaseListResult databaseAccountsListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**GremlinDatabaseListResult**](GremlinDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListGremlinGraphs

> GremlinGraphListResult databaseAccountsListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**GremlinGraphListResult**](GremlinGraphListResult.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListMongoDBCollections

> MongoDBCollectionListResult databaseAccountsListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**MongoDBCollectionListResult**](MongoDBCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListMongoDBDatabases

> MongoDBDatabaseListResult databaseAccountsListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**MongoDBDatabaseListResult**](MongoDBDatabaseListResult.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**DatabaseAccountListReadOnlyKeysResult**](DatabaseAccountListReadOnlyKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListSqlContainers

> SqlContainerListResult databaseAccountsListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**SqlContainerListResult**](SqlContainerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListSqlDatabases

> SqlDatabaseListResult databaseAccountsListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**SqlDatabaseListResult**](SqlDatabaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseAccountsListTables

> TableListResult databaseAccountsListTables(subscriptionId, resourceGroupName, accountName, apiVersion)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
apiInstance.databaseAccountsListTables(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

### Return type

[**TableListResult**](TableListResult.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **regionParameterForOnline** | [**RegionForOnlineOffline**](RegionForOnlineOffline.md)| Cosmos DB region to online for the database account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsPatch

> DatabaseAccount databaseAccountsPatch(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters)



Patches the properties of an existing Azure Cosmos DB database account.

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateParameters = new CosmosDb.DatabaseAccountPatchParameters(); // DatabaseAccountPatchParameters | The tags parameter to patch for the current database account.
apiInstance.databaseAccountsPatch(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateParameters** | [**DatabaseAccountPatchParameters**](DatabaseAccountPatchParameters.md)| The tags parameter to patch for the current database account. | 

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **keyToRegenerate** | [**DatabaseAccountRegenerateKeyParameters**](DatabaseAccountRegenerateKeyParameters.md)| The name of the key to regenerate. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## databaseAccountsUpdateCassandraKeyspaceThroughput

> Throughput databaseAccountsUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra Keyspace.
apiInstance.databaseAccountsUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra Keyspace. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateCassandraTableThroughput

> Throughput databaseAccountsUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra table.
apiInstance.databaseAccountsUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra table. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateGremlinDatabaseThroughput

> Throughput databaseAccountsUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin database.
apiInstance.databaseAccountsUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin database. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateGremlinGraphThroughput

> Throughput databaseAccountsUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin graph.
apiInstance.databaseAccountsUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin graph. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateMongoDBCollectionThroughput

> Throughput databaseAccountsUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB collection.
apiInstance.databaseAccountsUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB collection. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateMongoDBDatabaseThroughput

> Throughput databaseAccountsUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB database.
apiInstance.databaseAccountsUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB database. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateSqlContainerThroughput

> Throughput databaseAccountsUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current SQL container.
apiInstance.databaseAccountsUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL container. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateSqlDatabaseThroughput

> Throughput databaseAccountsUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current SQL database.
apiInstance.databaseAccountsUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL database. | 

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseAccountsUpdateTableThroughput

> Throughput databaseAccountsUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters)



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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
let updateThroughputParameters = new CosmosDb.ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current Table.
apiInstance.databaseAccountsUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current Table. | 

### Return type

[**Throughput**](Throughput.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **filter** | **String**| An OData filter expression that describes a subset of usages to return. The supported parameter is name.value (name of the metric, can have an or of multiple names). | [optional] 

### Return type

[**UsagesResult**](UsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | 
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. The parameters that can be filtered are name.value (name of the metric, can have an or of multiple names), startTime, endTime, and timeGrain. The supported operator is eq. | 

### Return type

[**PercentileMetricListResult**](PercentileMetricListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

