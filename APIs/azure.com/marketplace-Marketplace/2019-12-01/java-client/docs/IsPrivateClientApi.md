# IsPrivateClientApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateStoreClientGet**](IsPrivateClientApi.md#privateStoreClientGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Marketplace/privateStoreClient/isPrivateClient |  |


<a id="privateStoreClientGet"></a>
# **privateStoreClientGet**
> privateStoreClientGet(apiVersion, subscriptionId)



Check if client is private or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IsPrivateClientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IsPrivateClientApi apiInstance = new IsPrivateClientApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    try {
      apiInstance.privateStoreClientGet(apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IsPrivateClientApi#privateStoreClientGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |

