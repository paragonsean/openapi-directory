# DatabaseColumnsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseColumnsGet**](DatabaseColumnsApi.md#databaseColumnsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns/{columnName} |  |
| [**databaseColumnsListByTable**](DatabaseColumnsApi.md#databaseColumnsListByTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/schemas/{schemaName}/tables/{tableName}/columns |  |


<a id="databaseColumnsGet"></a>
# **databaseColumnsGet**
> DatabaseColumn databaseColumnsGet(resourceGroupName, serverName, databaseName, schemaName, tableName, columnName, subscriptionId, apiVersion)



Get database column

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseColumnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseColumnsApi apiInstance = new DatabaseColumnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String schemaName = "schemaName_example"; // String | The name of the schema.
    String tableName = "tableName_example"; // String | The name of the table.
    String columnName = "columnName_example"; // String | The name of the column.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      DatabaseColumn result = apiInstance.databaseColumnsGet(resourceGroupName, serverName, databaseName, schemaName, tableName, columnName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseColumnsApi#databaseColumnsGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **schemaName** | **String**| The name of the schema. | |
| **tableName** | **String**| The name of the table. | |
| **columnName** | **String**| The name of the column. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**DatabaseColumn**](DatabaseColumn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved database column. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 InvalidDatabaseSchema - Schema is missing in database.   * 404 InvalidDatabaseTable - Table is missing in database.   * 404 InvalidDatabaseColumn - Column is missing in table. |  -  |

<a id="databaseColumnsListByTable"></a>
# **databaseColumnsListByTable**
> DatabaseColumnListResult databaseColumnsListByTable(resourceGroupName, serverName, databaseName, schemaName, tableName, subscriptionId, apiVersion, $filter)



List database columns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseColumnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseColumnsApi apiInstance = new DatabaseColumnsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String schemaName = "schemaName_example"; // String | The name of the schema.
    String tableName = "tableName_example"; // String | The name of the table.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String $filter = "$filter_example"; // String | An OData filter expression that filters elements in the collection.
    try {
      DatabaseColumnListResult result = apiInstance.databaseColumnsListByTable(resourceGroupName, serverName, databaseName, schemaName, tableName, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseColumnsApi#databaseColumnsListByTable");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **schemaName** | **String**| The name of the schema. | |
| **tableName** | **String**| The name of the table. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **$filter** | **String**| An OData filter expression that filters elements in the collection. | [optional] |

### Return type

[**DatabaseColumnListResult**](DatabaseColumnListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved database columns. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 SourceDatabaseNotFound - The source database does not exist.   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 InvalidDatabaseSchema - Schema is missing in database.   * 404 InvalidDatabaseTable - Table is missing in database.   * 404 InvalidDatabaseColumn - Column is missing in table. |  -  |

