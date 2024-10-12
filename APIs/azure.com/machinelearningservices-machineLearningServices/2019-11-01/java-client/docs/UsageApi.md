# UsageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usagesList**](UsageApi.md#usagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/usages |  |


<a id="usagesList"></a>
# **usagesList**
> ListUsagesResult usagesList(apiVersion, subscriptionId, location)



Gets the current usage information as well as limits for AML resources for given subscription and location.

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
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    String location = "location_example"; // String | The location for which resource usage is queried.
    try {
      ListUsagesResult result = apiInstance.usagesList(apiVersion, subscriptionId, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsageApi#usagesList");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |
| **location** | **String**| The location for which resource usage is queried. | |

### Return type

[**ListUsagesResult**](ListUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

