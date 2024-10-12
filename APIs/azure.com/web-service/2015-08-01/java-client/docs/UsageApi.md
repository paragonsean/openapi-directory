# UsageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usageGetUsage**](UsageApi.md#usageGetUsage) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web.Admin/environments/{environmentName}/usage | Returns usage records for specified subscription and resource groups |


<a id="usageGetUsage"></a>
# **usageGetUsage**
> Object usageGetUsage(resourceGroupName, environmentName, lastId, batchSize, subscriptionId, apiVersion)

Returns usage records for specified subscription and resource groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsageApi apiInstance = new UsageApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String environmentName = "environmentName_example"; // String | Environment name
    String lastId = "lastId_example"; // String | Last marker that was returned from the batch
    Integer batchSize = 56; // Integer | size of the batch to be returned.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.usageGetUsage(resourceGroupName, environmentName, lastId, batchSize, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageApi#usageGetUsage");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **environmentName** | **String**| Environment name | |
| **lastId** | **String**| Last marker that was returned from the batch | |
| **batchSize** | **Integer**| size of the batch to be returned. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

