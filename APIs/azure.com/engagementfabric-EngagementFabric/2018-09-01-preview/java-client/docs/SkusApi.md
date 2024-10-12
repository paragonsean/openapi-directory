# SkusApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sKUsList**](SkusApi.md#sKUsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EngagementFabric/skus | List available SKUs of EngagementFabric resource |


<a id="sKUsList"></a>
# **sKUsList**
> SkuDescriptionList sKUsList(subscriptionId, apiVersion)

List available SKUs of EngagementFabric resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SkusApi apiInstance = new SkusApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      SkuDescriptionList result = apiInstance.sKUsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkusApi#sKUsList");
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
| **subscriptionId** | **String**| Subscription ID | |
| **apiVersion** | **String**| API version | |

### Return type

[**SkuDescriptionList**](SkuDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

