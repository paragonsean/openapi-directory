# RegionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**regionsListBySku**](RegionsApi.md#regionsListBySku) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/sku/{sku}/regions |  |


<a id="regionsListBySku"></a>
# **regionsListBySku**
> PremiumMessagingRegionsListResult regionsListBySku(apiVersion, subscriptionId, sku)



Gets the available Regions for a given sku

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String sku = "sku_example"; // String | The sku type.
    try {
      PremiumMessagingRegionsListResult result = apiInstance.regionsListBySku(apiVersion, subscriptionId, sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#regionsListBySku");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **sku** | **String**| The sku type. | |

### Return type

[**PremiumMessagingRegionsListResult**](PremiumMessagingRegionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Regions successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

