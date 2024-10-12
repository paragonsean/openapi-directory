# PremiumMessagingRegionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**premiumMessagingRegionsList**](PremiumMessagingRegionsApi.md#premiumMessagingRegionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/premiumMessagingRegions |  |


<a id="premiumMessagingRegionsList"></a>
# **premiumMessagingRegionsList**
> PremiumMessagingRegionsListResult premiumMessagingRegionsList(apiVersion, subscriptionId)



Gets the available premium messaging regions for servicebus 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PremiumMessagingRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PremiumMessagingRegionsApi apiInstance = new PremiumMessagingRegionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PremiumMessagingRegionsListResult result = apiInstance.premiumMessagingRegionsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PremiumMessagingRegionsApi#premiumMessagingRegionsList");
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
| **200** | Premium messaging regions successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

