# CheckResourceUsageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceUsageList**](CheckResourceUsageApi.md#resourceUsageList) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/checkResourceUsage |  |


<a id="resourceUsageList"></a>
# **resourceUsageList**
> ResourceUsageListResult resourceUsageList(subscriptionId, apiVersion)



Check the quota and actual usage of the CDN profiles under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckResourceUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckResourceUsageApi apiInstance = new CheckResourceUsageApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      ResourceUsageListResult result = apiInstance.resourceUsageList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckResourceUsageApi#resourceUsageList");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**ResourceUsageListResult**](ResourceUsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

