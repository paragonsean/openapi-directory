# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
| [**databaseAccountsCreateUpdateCassandraKeyspace**](DefaultApi.md#databaseAccountsCreateUpdateCassandraKeyspace) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} |  |
| [**databaseAccountsCreateUpdateCassandraTable**](DefaultApi.md#databaseAccountsCreateUpdateCassandraTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} |  |
| [**databaseAccountsCreateUpdateGremlinDatabase**](DefaultApi.md#databaseAccountsCreateUpdateGremlinDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} |  |
| [**databaseAccountsCreateUpdateGremlinGraph**](DefaultApi.md#databaseAccountsCreateUpdateGremlinGraph) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} |  |
| [**databaseAccountsCreateUpdateMongoDBCollection**](DefaultApi.md#databaseAccountsCreateUpdateMongoDBCollection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} |  |
| [**databaseAccountsCreateUpdateMongoDBDatabase**](DefaultApi.md#databaseAccountsCreateUpdateMongoDBDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} |  |
| [**databaseAccountsCreateUpdateSqlContainer**](DefaultApi.md#databaseAccountsCreateUpdateSqlContainer) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} |  |
| [**databaseAccountsCreateUpdateSqlDatabase**](DefaultApi.md#databaseAccountsCreateUpdateSqlDatabase) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} |  |
| [**databaseAccountsCreateUpdateTable**](DefaultApi.md#databaseAccountsCreateUpdateTable) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} |  |
| [**databaseAccountsDelete**](DefaultApi.md#databaseAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsDeleteCassandraKeyspace**](DefaultApi.md#databaseAccountsDeleteCassandraKeyspace) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} |  |
| [**databaseAccountsDeleteCassandraTable**](DefaultApi.md#databaseAccountsDeleteCassandraTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} |  |
| [**databaseAccountsDeleteGremlinDatabase**](DefaultApi.md#databaseAccountsDeleteGremlinDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} |  |
| [**databaseAccountsDeleteGremlinGraph**](DefaultApi.md#databaseAccountsDeleteGremlinGraph) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} |  |
| [**databaseAccountsDeleteMongoDBCollection**](DefaultApi.md#databaseAccountsDeleteMongoDBCollection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} |  |
| [**databaseAccountsDeleteMongoDBDatabase**](DefaultApi.md#databaseAccountsDeleteMongoDBDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} |  |
| [**databaseAccountsDeleteSqlContainer**](DefaultApi.md#databaseAccountsDeleteSqlContainer) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} |  |
| [**databaseAccountsDeleteSqlDatabase**](DefaultApi.md#databaseAccountsDeleteSqlDatabase) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} |  |
| [**databaseAccountsDeleteTable**](DefaultApi.md#databaseAccountsDeleteTable) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} |  |
| [**databaseAccountsFailoverPriorityChange**](DefaultApi.md#databaseAccountsFailoverPriorityChange) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/failoverPriorityChange |  |
| [**databaseAccountsGet**](DefaultApi.md#databaseAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsGetCassandraKeyspace**](DefaultApi.md#databaseAccountsGetCassandraKeyspace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName} |  |
| [**databaseAccountsGetCassandraKeyspaceThroughput**](DefaultApi.md#databaseAccountsGetCassandraKeyspaceThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/settings/throughput |  |
| [**databaseAccountsGetCassandraTable**](DefaultApi.md#databaseAccountsGetCassandraTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName} |  |
| [**databaseAccountsGetCassandraTableThroughput**](DefaultApi.md#databaseAccountsGetCassandraTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName}/settings/throughput |  |
| [**databaseAccountsGetGremlinDatabase**](DefaultApi.md#databaseAccountsGetGremlinDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName} |  |
| [**databaseAccountsGetGremlinDatabaseThroughput**](DefaultApi.md#databaseAccountsGetGremlinDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsGetGremlinGraph**](DefaultApi.md#databaseAccountsGetGremlinGraph) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName} |  |
| [**databaseAccountsGetGremlinGraphThroughput**](DefaultApi.md#databaseAccountsGetGremlinGraphThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName}/settings/throughput |  |
| [**databaseAccountsGetMongoDBCollection**](DefaultApi.md#databaseAccountsGetMongoDBCollection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName} |  |
| [**databaseAccountsGetMongoDBCollectionThroughput**](DefaultApi.md#databaseAccountsGetMongoDBCollectionThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName}/settings/throughput |  |
| [**databaseAccountsGetMongoDBDatabase**](DefaultApi.md#databaseAccountsGetMongoDBDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName} |  |
| [**databaseAccountsGetMongoDBDatabaseThroughput**](DefaultApi.md#databaseAccountsGetMongoDBDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsGetReadOnlyKeys**](DefaultApi.md#databaseAccountsGetReadOnlyKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys |  |
| [**databaseAccountsGetSqlContainer**](DefaultApi.md#databaseAccountsGetSqlContainer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName} |  |
| [**databaseAccountsGetSqlContainerThroughput**](DefaultApi.md#databaseAccountsGetSqlContainerThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName}/settings/throughput |  |
| [**databaseAccountsGetSqlDatabase**](DefaultApi.md#databaseAccountsGetSqlDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName} |  |
| [**databaseAccountsGetSqlDatabaseThroughput**](DefaultApi.md#databaseAccountsGetSqlDatabaseThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsGetTable**](DefaultApi.md#databaseAccountsGetTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName} |  |
| [**databaseAccountsGetTableThroughput**](DefaultApi.md#databaseAccountsGetTableThroughput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName}/settings/throughput |  |
| [**databaseAccountsList**](DefaultApi.md#databaseAccountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/databaseAccounts |  |
| [**databaseAccountsListByResourceGroup**](DefaultApi.md#databaseAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts |  |
| [**databaseAccountsListCassandraKeyspaces**](DefaultApi.md#databaseAccountsListCassandraKeyspaces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces |  |
| [**databaseAccountsListCassandraTables**](DefaultApi.md#databaseAccountsListCassandraTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables |  |
| [**databaseAccountsListConnectionStrings**](DefaultApi.md#databaseAccountsListConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listConnectionStrings |  |
| [**databaseAccountsListGremlinDatabases**](DefaultApi.md#databaseAccountsListGremlinDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases |  |
| [**databaseAccountsListGremlinGraphs**](DefaultApi.md#databaseAccountsListGremlinGraphs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs |  |
| [**databaseAccountsListKeys**](DefaultApi.md#databaseAccountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/listKeys |  |
| [**databaseAccountsListMetricDefinitions**](DefaultApi.md#databaseAccountsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metricDefinitions |  |
| [**databaseAccountsListMetrics**](DefaultApi.md#databaseAccountsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/metrics |  |
| [**databaseAccountsListMongoDBCollections**](DefaultApi.md#databaseAccountsListMongoDBCollections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections |  |
| [**databaseAccountsListMongoDBDatabases**](DefaultApi.md#databaseAccountsListMongoDBDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases |  |
| [**databaseAccountsListReadOnlyKeys**](DefaultApi.md#databaseAccountsListReadOnlyKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/readonlykeys |  |
| [**databaseAccountsListSqlContainers**](DefaultApi.md#databaseAccountsListSqlContainers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers |  |
| [**databaseAccountsListSqlDatabases**](DefaultApi.md#databaseAccountsListSqlDatabases) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases |  |
| [**databaseAccountsListTables**](DefaultApi.md#databaseAccountsListTables) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables |  |
| [**databaseAccountsListUsages**](DefaultApi.md#databaseAccountsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/usages |  |
| [**databaseAccountsOfflineRegion**](DefaultApi.md#databaseAccountsOfflineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/offlineRegion |  |
| [**databaseAccountsOnlineRegion**](DefaultApi.md#databaseAccountsOnlineRegion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/onlineRegion |  |
| [**databaseAccountsPatch**](DefaultApi.md#databaseAccountsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName} |  |
| [**databaseAccountsRegenerateKey**](DefaultApi.md#databaseAccountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/regenerateKey |  |
| [**databaseAccountsUpdateCassandraKeyspaceThroughput**](DefaultApi.md#databaseAccountsUpdateCassandraKeyspaceThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/settings/throughput |  |
| [**databaseAccountsUpdateCassandraTableThroughput**](DefaultApi.md#databaseAccountsUpdateCassandraTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/cassandra/keyspaces/{keyspaceName}/tables/{tableName}/settings/throughput |  |
| [**databaseAccountsUpdateGremlinDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateGremlinDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsUpdateGremlinGraphThroughput**](DefaultApi.md#databaseAccountsUpdateGremlinGraphThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/gremlin/databases/{databaseName}/graphs/{graphName}/settings/throughput |  |
| [**databaseAccountsUpdateMongoDBCollectionThroughput**](DefaultApi.md#databaseAccountsUpdateMongoDBCollectionThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/collections/{collectionName}/settings/throughput |  |
| [**databaseAccountsUpdateMongoDBDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateMongoDBDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/mongodb/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsUpdateSqlContainerThroughput**](DefaultApi.md#databaseAccountsUpdateSqlContainerThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/containers/{containerName}/settings/throughput |  |
| [**databaseAccountsUpdateSqlDatabaseThroughput**](DefaultApi.md#databaseAccountsUpdateSqlDatabaseThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/sql/databases/{databaseName}/settings/throughput |  |
| [**databaseAccountsUpdateTableThroughput**](DefaultApi.md#databaseAccountsUpdateTableThroughput) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/apis/table/tables/{tableName}/settings/throughput |  |
| [**databaseListMetricDefinitions**](DefaultApi.md#databaseListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metricDefinitions |  |
| [**databaseListMetrics**](DefaultApi.md#databaseListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metrics |  |
| [**databaseListUsages**](DefaultApi.md#databaseListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/usages |  |
| [**partitionKeyRangeIdListMetrics**](DefaultApi.md#partitionKeyRangeIdListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics |  |
| [**partitionKeyRangeIdRegionListMetrics**](DefaultApi.md#partitionKeyRangeIdRegionListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics |  |
| [**percentileListMetrics**](DefaultApi.md#percentileListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/percentile/metrics |  |
| [**percentileSourceTargetListMetrics**](DefaultApi.md#percentileSourceTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/sourceRegion/{sourceRegion}/targetRegion/{targetRegion}/percentile/metrics |  |
| [**percentileTargetListMetrics**](DefaultApi.md#percentileTargetListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/targetRegion/{targetRegion}/percentile/metrics |  |


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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
> DatabaseAccount databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters)



Creates or updates an Azure Cosmos DB database account.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    DatabaseAccountCreateUpdateParameters createUpdateParameters = new DatabaseAccountCreateUpdateParameters(); // DatabaseAccountCreateUpdateParameters | The parameters to provide for the current database account.
    try {
      DatabaseAccount result = apiInstance.databaseAccountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, createUpdateParameters);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateParameters** | [**DatabaseAccountCreateUpdateParameters**](DatabaseAccountCreateUpdateParameters.md)| The parameters to provide for the current database account. | |

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database account create or update operation will complete asynchronously. |  -  |

<a id="databaseAccountsCreateUpdateCassandraKeyspace"></a>
# **databaseAccountsCreateUpdateCassandraKeyspace**
> CassandraKeyspace databaseAccountsCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    CassandraKeyspaceCreateUpdateParameters createUpdateCassandraKeyspaceParameters = new CassandraKeyspaceCreateUpdateParameters(); // CassandraKeyspaceCreateUpdateParameters | The parameters to provide for the current Cassandra keyspace.
    try {
      CassandraKeyspace result = apiInstance.databaseAccountsCreateUpdateCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, createUpdateCassandraKeyspaceParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateCassandraKeyspace");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateCassandraKeyspaceParameters** | [**CassandraKeyspaceCreateUpdateParameters**](CassandraKeyspaceCreateUpdateParameters.md)| The parameters to provide for the current Cassandra keyspace. | |

### Return type

[**CassandraKeyspace**](CassandraKeyspace.md)

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

<a id="databaseAccountsCreateUpdateCassandraTable"></a>
# **databaseAccountsCreateUpdateCassandraTable**
> CassandraTable databaseAccountsCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    CassandraTableCreateUpdateParameters createUpdateCassandraTableParameters = new CassandraTableCreateUpdateParameters(); // CassandraTableCreateUpdateParameters | The parameters to provide for the current Cassandra Table.
    try {
      CassandraTable result = apiInstance.databaseAccountsCreateUpdateCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, createUpdateCassandraTableParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateCassandraTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateCassandraTableParameters** | [**CassandraTableCreateUpdateParameters**](CassandraTableCreateUpdateParameters.md)| The parameters to provide for the current Cassandra Table. | |

### Return type

[**CassandraTable**](CassandraTable.md)

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

<a id="databaseAccountsCreateUpdateGremlinDatabase"></a>
# **databaseAccountsCreateUpdateGremlinDatabase**
> GremlinDatabase databaseAccountsCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    GremlinDatabaseCreateUpdateParameters createUpdateGremlinDatabaseParameters = new GremlinDatabaseCreateUpdateParameters(); // GremlinDatabaseCreateUpdateParameters | The parameters to provide for the current Gremlin database.
    try {
      GremlinDatabase result = apiInstance.databaseAccountsCreateUpdateGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateGremlinDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateGremlinDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateGremlinDatabaseParameters** | [**GremlinDatabaseCreateUpdateParameters**](GremlinDatabaseCreateUpdateParameters.md)| The parameters to provide for the current Gremlin database. | |

### Return type

[**GremlinDatabase**](GremlinDatabase.md)

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

<a id="databaseAccountsCreateUpdateGremlinGraph"></a>
# **databaseAccountsCreateUpdateGremlinGraph**
> GremlinGraph databaseAccountsCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    GremlinGraphCreateUpdateParameters createUpdateGremlinGraphParameters = new GremlinGraphCreateUpdateParameters(); // GremlinGraphCreateUpdateParameters | The parameters to provide for the current Gremlin graph.
    try {
      GremlinGraph result = apiInstance.databaseAccountsCreateUpdateGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, createUpdateGremlinGraphParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateGremlinGraph");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateGremlinGraphParameters** | [**GremlinGraphCreateUpdateParameters**](GremlinGraphCreateUpdateParameters.md)| The parameters to provide for the current Gremlin graph. | |

### Return type

[**GremlinGraph**](GremlinGraph.md)

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

<a id="databaseAccountsCreateUpdateMongoDBCollection"></a>
# **databaseAccountsCreateUpdateMongoDBCollection**
> MongoDBCollection databaseAccountsCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    MongoDBCollectionCreateUpdateParameters createUpdateMongoDBCollectionParameters = new MongoDBCollectionCreateUpdateParameters(); // MongoDBCollectionCreateUpdateParameters | The parameters to provide for the current MongoDB Collection.
    try {
      MongoDBCollection result = apiInstance.databaseAccountsCreateUpdateMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, createUpdateMongoDBCollectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateMongoDBCollection");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateMongoDBCollectionParameters** | [**MongoDBCollectionCreateUpdateParameters**](MongoDBCollectionCreateUpdateParameters.md)| The parameters to provide for the current MongoDB Collection. | |

### Return type

[**MongoDBCollection**](MongoDBCollection.md)

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

<a id="databaseAccountsCreateUpdateMongoDBDatabase"></a>
# **databaseAccountsCreateUpdateMongoDBDatabase**
> MongoDBDatabase databaseAccountsCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    MongoDBDatabaseCreateUpdateParameters createUpdateMongoDBDatabaseParameters = new MongoDBDatabaseCreateUpdateParameters(); // MongoDBDatabaseCreateUpdateParameters | The parameters to provide for the current MongoDB database.
    try {
      MongoDBDatabase result = apiInstance.databaseAccountsCreateUpdateMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateMongoDBDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateMongoDBDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateMongoDBDatabaseParameters** | [**MongoDBDatabaseCreateUpdateParameters**](MongoDBDatabaseCreateUpdateParameters.md)| The parameters to provide for the current MongoDB database. | |

### Return type

[**MongoDBDatabase**](MongoDBDatabase.md)

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

<a id="databaseAccountsCreateUpdateSqlContainer"></a>
# **databaseAccountsCreateUpdateSqlContainer**
> SqlContainer databaseAccountsCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    SqlContainerCreateUpdateParameters createUpdateSqlContainerParameters = new SqlContainerCreateUpdateParameters(); // SqlContainerCreateUpdateParameters | The parameters to provide for the current SQL container.
    try {
      SqlContainer result = apiInstance.databaseAccountsCreateUpdateSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, createUpdateSqlContainerParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateSqlContainer");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateSqlContainerParameters** | [**SqlContainerCreateUpdateParameters**](SqlContainerCreateUpdateParameters.md)| The parameters to provide for the current SQL container. | |

### Return type

[**SqlContainer**](SqlContainer.md)

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

<a id="databaseAccountsCreateUpdateSqlDatabase"></a>
# **databaseAccountsCreateUpdateSqlDatabase**
> SqlDatabase databaseAccountsCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    SqlDatabaseCreateUpdateParameters createUpdateSqlDatabaseParameters = new SqlDatabaseCreateUpdateParameters(); // SqlDatabaseCreateUpdateParameters | The parameters to provide for the current SQL database.
    try {
      SqlDatabase result = apiInstance.databaseAccountsCreateUpdateSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, createUpdateSqlDatabaseParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateSqlDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateSqlDatabaseParameters** | [**SqlDatabaseCreateUpdateParameters**](SqlDatabaseCreateUpdateParameters.md)| The parameters to provide for the current SQL database. | |

### Return type

[**SqlDatabase**](SqlDatabase.md)

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

<a id="databaseAccountsCreateUpdateTable"></a>
# **databaseAccountsCreateUpdateTable**
> Table databaseAccountsCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    TableCreateUpdateParameters createUpdateTableParameters = new TableCreateUpdateParameters(); // TableCreateUpdateParameters | The parameters to provide for the current Table.
    try {
      Table result = apiInstance.databaseAccountsCreateUpdateTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, createUpdateTableParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsCreateUpdateTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **createUpdateTableParameters** | [**TableCreateUpdateParameters**](TableCreateUpdateParameters.md)| The parameters to provide for the current Table. | |

### Return type

[**Table**](Table.md)

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteCassandraKeyspace"></a>
# **databaseAccountsDeleteCassandraKeyspace**
> databaseAccountsDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteCassandraKeyspace");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteCassandraTable"></a>
# **databaseAccountsDeleteCassandraTable**
> databaseAccountsDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteCassandraTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteGremlinDatabase"></a>
# **databaseAccountsDeleteGremlinDatabase**
> databaseAccountsDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteGremlinDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteGremlinGraph"></a>
# **databaseAccountsDeleteGremlinGraph**
> databaseAccountsDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteGremlinGraph");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteMongoDBCollection"></a>
# **databaseAccountsDeleteMongoDBCollection**
> databaseAccountsDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteMongoDBCollection");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteMongoDBDatabase"></a>
# **databaseAccountsDeleteMongoDBDatabase**
> databaseAccountsDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteMongoDBDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteSqlContainer"></a>
# **databaseAccountsDeleteSqlContainer**
> databaseAccountsDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteSqlContainer");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteSqlDatabase"></a>
# **databaseAccountsDeleteSqlDatabase**
> databaseAccountsDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteSqlDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsDeleteTable"></a>
# **databaseAccountsDeleteTable**
> databaseAccountsDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      apiInstance.databaseAccountsDeleteTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsDeleteTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
> DatabaseAccount databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      DatabaseAccount result = apiInstance.databaseAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The database account properties were retrieved successfully. |  -  |

<a id="databaseAccountsGetCassandraKeyspace"></a>
# **databaseAccountsGetCassandraKeyspace**
> CassandraKeyspace databaseAccountsGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      CassandraKeyspace result = apiInstance.databaseAccountsGetCassandraKeyspace(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetCassandraKeyspace");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**CassandraKeyspace**](CassandraKeyspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra keyspace property was retrieved successfully. |  -  |

<a id="databaseAccountsGetCassandraKeyspaceThroughput"></a>
# **databaseAccountsGetCassandraKeyspaceThroughput**
> Throughput databaseAccountsGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetCassandraKeyspaceThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra Keyspace was retrieved successfully. |  -  |

<a id="databaseAccountsGetCassandraTable"></a>
# **databaseAccountsGetCassandraTable**
> CassandraTable databaseAccountsGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      CassandraTable result = apiInstance.databaseAccountsGetCassandraTable(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetCassandraTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**CassandraTable**](CassandraTable.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Cassandra table property was retrieved successfully. |  -  |

<a id="databaseAccountsGetCassandraTableThroughput"></a>
# **databaseAccountsGetCassandraTableThroughput**
> Throughput databaseAccountsGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetCassandraTableThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Cassandra table was retrieved successfully. |  -  |

<a id="databaseAccountsGetGremlinDatabase"></a>
# **databaseAccountsGetGremlinDatabase**
> GremlinDatabase databaseAccountsGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      GremlinDatabase result = apiInstance.databaseAccountsGetGremlinDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetGremlinDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**GremlinDatabase**](GremlinDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin database property was retrieved successfully. |  -  |

<a id="databaseAccountsGetGremlinDatabaseThroughput"></a>
# **databaseAccountsGetGremlinDatabaseThroughput**
> Throughput databaseAccountsGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetGremlinDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin database was retrieved successfully. |  -  |

<a id="databaseAccountsGetGremlinGraph"></a>
# **databaseAccountsGetGremlinGraph**
> GremlinGraph databaseAccountsGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      GremlinGraph result = apiInstance.databaseAccountsGetGremlinGraph(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetGremlinGraph");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**GremlinGraph**](GremlinGraph.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Gremlin graph property was retrieved successfully. |  -  |

<a id="databaseAccountsGetGremlinGraphThroughput"></a>
# **databaseAccountsGetGremlinGraphThroughput**
> Throughput databaseAccountsGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetGremlinGraphThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Gremlin graph was retrieved successfully. |  -  |

<a id="databaseAccountsGetMongoDBCollection"></a>
# **databaseAccountsGetMongoDBCollection**
> MongoDBCollection databaseAccountsGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      MongoDBCollection result = apiInstance.databaseAccountsGetMongoDBCollection(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetMongoDBCollection");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**MongoDBCollection**](MongoDBCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB collection property was retrieved successfully. |  -  |

<a id="databaseAccountsGetMongoDBCollectionThroughput"></a>
# **databaseAccountsGetMongoDBCollectionThroughput**
> Throughput databaseAccountsGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetMongoDBCollectionThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB collection was retrieved successfully. |  -  |

<a id="databaseAccountsGetMongoDBDatabase"></a>
# **databaseAccountsGetMongoDBDatabase**
> MongoDBDatabase databaseAccountsGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      MongoDBDatabase result = apiInstance.databaseAccountsGetMongoDBDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetMongoDBDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**MongoDBDatabase**](MongoDBDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MongoDB database property was retrieved successfully. |  -  |

<a id="databaseAccountsGetMongoDBDatabaseThroughput"></a>
# **databaseAccountsGetMongoDBDatabaseThroughput**
> Throughput databaseAccountsGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetMongoDBDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the MongoDB database was retrieved successfully. |  -  |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsGetSqlContainer"></a>
# **databaseAccountsGetSqlContainer**
> SqlContainer databaseAccountsGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      SqlContainer result = apiInstance.databaseAccountsGetSqlContainer(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetSqlContainer");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**SqlContainer**](SqlContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL container property was retrieved successfully. |  -  |

<a id="databaseAccountsGetSqlContainerThroughput"></a>
# **databaseAccountsGetSqlContainerThroughput**
> Throughput databaseAccountsGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetSqlContainerThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL container was retrieved successfully. |  -  |

<a id="databaseAccountsGetSqlDatabase"></a>
# **databaseAccountsGetSqlDatabase**
> SqlDatabase databaseAccountsGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      SqlDatabase result = apiInstance.databaseAccountsGetSqlDatabase(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetSqlDatabase");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**SqlDatabase**](SqlDatabase.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The SQL database property was retrieved successfully. |  -  |

<a id="databaseAccountsGetSqlDatabaseThroughput"></a>
# **databaseAccountsGetSqlDatabaseThroughput**
> Throughput databaseAccountsGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetSqlDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the SQL database was retrieved successfully. |  -  |

<a id="databaseAccountsGetTable"></a>
# **databaseAccountsGetTable**
> Table databaseAccountsGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Table result = apiInstance.databaseAccountsGetTable(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetTable");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Table**](Table.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Table property was retrieved successfully. |  -  |

<a id="databaseAccountsGetTableThroughput"></a>
# **databaseAccountsGetTableThroughput**
> Throughput databaseAccountsGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      Throughput result = apiInstance.databaseAccountsGetTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsGetTableThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

### Return type

[**Throughput**](Throughput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RUs per second of the Table was retrieved successfully. |  -  |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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

<a id="databaseAccountsListCassandraKeyspaces"></a>
# **databaseAccountsListCassandraKeyspaces**
> CassandraKeyspaceListResult databaseAccountsListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      CassandraKeyspaceListResult result = apiInstance.databaseAccountsListCassandraKeyspaces(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListCassandraKeyspaces");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListCassandraTables"></a>
# **databaseAccountsListCassandraTables**
> CassandraTableListResult databaseAccountsListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      CassandraTableListResult result = apiInstance.databaseAccountsListCassandraTables(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListCassandraTables");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListGremlinDatabases"></a>
# **databaseAccountsListGremlinDatabases**
> GremlinDatabaseListResult databaseAccountsListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      GremlinDatabaseListResult result = apiInstance.databaseAccountsListGremlinDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListGremlinDatabases");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListGremlinGraphs"></a>
# **databaseAccountsListGremlinGraphs**
> GremlinGraphListResult databaseAccountsListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      GremlinGraphListResult result = apiInstance.databaseAccountsListGremlinGraphs(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListGremlinGraphs");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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

<a id="databaseAccountsListMongoDBCollections"></a>
# **databaseAccountsListMongoDBCollections**
> MongoDBCollectionListResult databaseAccountsListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      MongoDBCollectionListResult result = apiInstance.databaseAccountsListMongoDBCollections(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListMongoDBCollections");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListMongoDBDatabases"></a>
# **databaseAccountsListMongoDBDatabases**
> MongoDBDatabaseListResult databaseAccountsListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      MongoDBDatabaseListResult result = apiInstance.databaseAccountsListMongoDBDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListMongoDBDatabases");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListSqlContainers"></a>
# **databaseAccountsListSqlContainers**
> SqlContainerListResult databaseAccountsListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      SqlContainerListResult result = apiInstance.databaseAccountsListSqlContainers(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListSqlContainers");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListSqlDatabases"></a>
# **databaseAccountsListSqlDatabases**
> SqlDatabaseListResult databaseAccountsListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      SqlDatabaseListResult result = apiInstance.databaseAccountsListSqlDatabases(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListSqlDatabases");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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

<a id="databaseAccountsListTables"></a>
# **databaseAccountsListTables**
> TableListResult databaseAccountsListTables(subscriptionId, resourceGroupName, accountName, apiVersion)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    try {
      TableListResult result = apiInstance.databaseAccountsListTables(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsListTables");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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

<a id="databaseAccountsPatch"></a>
# **databaseAccountsPatch**
> DatabaseAccount databaseAccountsPatch(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters)



Patches the properties of an existing Azure Cosmos DB database account.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    DatabaseAccountPatchParameters updateParameters = new DatabaseAccountPatchParameters(); // DatabaseAccountPatchParameters | The tags parameter to patch for the current database account.
    try {
      DatabaseAccount result = apiInstance.databaseAccountsPatch(subscriptionId, resourceGroupName, accountName, apiVersion, updateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsPatch");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateParameters** | [**DatabaseAccountPatchParameters**](DatabaseAccountPatchParameters.md)| The tags parameter to patch for the current database account. | |

### Return type

[**DatabaseAccount**](DatabaseAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The properties of the database account were patched successfully. |  -  |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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

<a id="databaseAccountsUpdateCassandraKeyspaceThroughput"></a>
# **databaseAccountsUpdateCassandraKeyspaceThroughput**
> Throughput databaseAccountsUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra Keyspace.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateCassandraKeyspaceThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateCassandraKeyspaceThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra Keyspace. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateCassandraTableThroughput"></a>
# **databaseAccountsUpdateCassandraTableThroughput**
> Throughput databaseAccountsUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Cassandra table.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateCassandraTableThroughput(subscriptionId, resourceGroupName, accountName, keyspaceName, tableName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateCassandraTableThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Cassandra table. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateGremlinDatabaseThroughput"></a>
# **databaseAccountsUpdateGremlinDatabaseThroughput**
> Throughput databaseAccountsUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin database.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateGremlinDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateGremlinDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin database. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateGremlinGraphThroughput"></a>
# **databaseAccountsUpdateGremlinGraphThroughput**
> Throughput databaseAccountsUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current Gremlin graph.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateGremlinGraphThroughput(subscriptionId, resourceGroupName, accountName, databaseName, graphName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateGremlinGraphThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current Gremlin graph. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateMongoDBCollectionThroughput"></a>
# **databaseAccountsUpdateMongoDBCollectionThroughput**
> Throughput databaseAccountsUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB collection.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateMongoDBCollectionThroughput(subscriptionId, resourceGroupName, accountName, databaseName, collectionName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateMongoDBCollectionThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB collection. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateMongoDBDatabaseThroughput"></a>
# **databaseAccountsUpdateMongoDBDatabaseThroughput**
> Throughput databaseAccountsUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The RUs per second of the parameters to provide for the current MongoDB database.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateMongoDBDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateMongoDBDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The RUs per second of the parameters to provide for the current MongoDB database. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateSqlContainerThroughput"></a>
# **databaseAccountsUpdateSqlContainerThroughput**
> Throughput databaseAccountsUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current SQL container.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateSqlContainerThroughput(subscriptionId, resourceGroupName, accountName, databaseName, containerName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateSqlContainerThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL container. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateSqlDatabaseThroughput"></a>
# **databaseAccountsUpdateSqlDatabaseThroughput**
> Throughput databaseAccountsUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current SQL database.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateSqlDatabaseThroughput(subscriptionId, resourceGroupName, accountName, databaseName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateSqlDatabaseThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current SQL database. | |

### Return type

[**Throughput**](Throughput.md)

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

<a id="databaseAccountsUpdateTableThroughput"></a>
# **databaseAccountsUpdateTableThroughput**
> Throughput databaseAccountsUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
    ThroughputUpdateParameters updateThroughputParameters = new ThroughputUpdateParameters(); // ThroughputUpdateParameters | The parameters to provide for the RUs per second of the current Table.
    try {
      Throughput result = apiInstance.databaseAccountsUpdateTableThroughput(subscriptionId, resourceGroupName, accountName, tableName, apiVersion, updateThroughputParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#databaseAccountsUpdateTableThroughput");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
| **updateThroughputParameters** | [**ThroughputUpdateParameters**](ThroughputUpdateParameters.md)| The parameters to provide for the RUs per second of the current Table. | |

### Return type

[**Throughput**](Throughput.md)

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2015-04-08.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2015-04-08. | |
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

