# DatabaseInstancesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseInstancesEnumerateDatabaseInstances**](DatabaseInstancesApi.md#databaseInstancesEnumerateDatabaseInstances) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databaseInstances | Gets a list of database instances in the migrate project. |
| [**databaseInstancesGetDatabaseInstance**](DatabaseInstancesApi.md#databaseInstancesGetDatabaseInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/databaseInstances/{databaseInstanceName} | Gets a database instance in the migrate project. |


<a id="databaseInstancesEnumerateDatabaseInstances"></a>
# **databaseInstancesEnumerateDatabaseInstances**
> DatabaseInstanceCollection databaseInstancesEnumerateDatabaseInstances(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize, acceptLanguage)

Gets a list of database instances in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatabaseInstancesApi apiInstance = new DatabaseInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String continuationToken = "continuationToken_example"; // String | The continuation token.
    Integer pageSize = 56; // Integer | The number of items to be returned in a single page. This value is honored only if it is less than the 100.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      DatabaseInstanceCollection result = apiInstance.databaseInstancesEnumerateDatabaseInstances(subscriptionId, resourceGroupName, migrateProjectName, apiVersion, continuationToken, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseInstancesApi#databaseInstancesEnumerateDatabaseInstances");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **continuationToken** | **String**| The continuation token. | [optional] |
| **pageSize** | **Integer**| The number of items to be returned in a single page. This value is honored only if it is less than the 100. | [optional] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**DatabaseInstanceCollection**](DatabaseInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="databaseInstancesGetDatabaseInstance"></a>
# **databaseInstancesGetDatabaseInstance**
> DatabaseInstance databaseInstancesGetDatabaseInstance(subscriptionId, resourceGroupName, migrateProjectName, databaseInstanceName, apiVersion, acceptLanguage)

Gets a database instance in the migrate project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DatabaseInstancesApi apiInstance = new DatabaseInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which migrate project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that migrate project is part of.
    String migrateProjectName = "migrateProjectName_example"; // String | Name of the Azure Migrate project.
    String databaseInstanceName = "databaseInstanceName_example"; // String | Unique name of a database instance in Azure migration hub.
    String apiVersion = "2018-09-01-preview"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      DatabaseInstance result = apiInstance.databaseInstancesGetDatabaseInstance(subscriptionId, resourceGroupName, migrateProjectName, databaseInstanceName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseInstancesApi#databaseInstancesGetDatabaseInstance");
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
| **subscriptionId** | **String**| Azure Subscription Id in which migrate project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that migrate project is part of. | |
| **migrateProjectName** | **String**| Name of the Azure Migrate project. | |
| **databaseInstanceName** | **String**| Unique name of a database instance in Azure migration hub. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-09-01-preview] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**DatabaseInstance**](DatabaseInstance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

