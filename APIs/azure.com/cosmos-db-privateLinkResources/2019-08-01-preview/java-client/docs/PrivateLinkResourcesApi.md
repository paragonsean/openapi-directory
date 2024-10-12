# PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateLinkResources/{groupName} |  |
| [**privateLinkResourcesListByDatabaseAccount**](PrivateLinkResourcesApi.md#privateLinkResourcesListByDatabaseAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateLinkResources |  |


<a id="privateLinkResourcesGet"></a>
# **privateLinkResourcesGet**
> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, accountName, groupName)



Gets the private link resources that need to be created for a Cosmos DB account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkResourcesApi apiInstance = new PrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    String groupName = "groupName_example"; // String | The name of the private link resource.
    try {
      PrivateLinkResource result = apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, accountName, groupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **accountName** | **String**| Cosmos DB database account name. | |
| **groupName** | **String**| The name of the private link resource. | |

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved a specified private link resource. |  -  |

<a id="privateLinkResourcesListByDatabaseAccount"></a>
# **privateLinkResourcesListByDatabaseAccount**
> PrivateLinkResourceListResult privateLinkResourcesListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName)



Gets the private link resources that need to be created for a Cosmos DB account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateLinkResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateLinkResourcesApi apiInstance = new PrivateLinkResourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
    String accountName = "accountName_example"; // String | Cosmos DB database account name.
    try {
      PrivateLinkResourceListResult result = apiInstance.privateLinkResourcesListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateLinkResourcesApi#privateLinkResourcesListByDatabaseAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | |
| **accountName** | **String**| Cosmos DB database account name. | |

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved private link resources. |  -  |

