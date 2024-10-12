# HealthApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkHealthAlerts_1**](HealthApi.md#getNetworkHealthAlerts_1) | **GET** /networks/{networkId}/health/alerts | Return all global alerts on this network |


<a id="getNetworkHealthAlerts_1"></a>
# **getNetworkHealthAlerts_1**
> List&lt;GetNetworkHealthAlerts200ResponseInner&gt; getNetworkHealthAlerts_1(networkId)

Return all global alerts on this network

Return all global alerts on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkHealthAlerts200ResponseInner> result = apiInstance.getNetworkHealthAlerts_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#getNetworkHealthAlerts_1");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkHealthAlerts200ResponseInner&gt;**](GetNetworkHealthAlerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

