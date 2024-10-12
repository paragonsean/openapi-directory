# TrafficAnalysisApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkTrafficAnalysis_1**](TrafficAnalysisApi.md#getNetworkTrafficAnalysis_1) | **GET** /networks/{networkId}/trafficAnalysis | Return the traffic analysis settings for a network |
| [**updateNetworkTrafficAnalysis_1**](TrafficAnalysisApi.md#updateNetworkTrafficAnalysis_1) | **PUT** /networks/{networkId}/trafficAnalysis | Update the traffic analysis settings for a network |


<a id="getNetworkTrafficAnalysis_1"></a>
# **getNetworkTrafficAnalysis_1**
> Object getNetworkTrafficAnalysis_1(networkId)

Return the traffic analysis settings for a network

Return the traffic analysis settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficAnalysisApi apiInstance = new TrafficAnalysisApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkTrafficAnalysis_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficAnalysisApi#getNetworkTrafficAnalysis_1");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkTrafficAnalysis_1"></a>
# **updateNetworkTrafficAnalysis_1**
> Object updateNetworkTrafficAnalysis_1(networkId, updateNetworkTrafficAnalysisRequest)

Update the traffic analysis settings for a network

Update the traffic analysis settings for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficAnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficAnalysisApi apiInstance = new TrafficAnalysisApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkTrafficAnalysisRequest updateNetworkTrafficAnalysisRequest = new UpdateNetworkTrafficAnalysisRequest(); // UpdateNetworkTrafficAnalysisRequest | 
    try {
      Object result = apiInstance.updateNetworkTrafficAnalysis_1(networkId, updateNetworkTrafficAnalysisRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficAnalysisApi#updateNetworkTrafficAnalysis_1");
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
| **updateNetworkTrafficAnalysisRequest** | [**UpdateNetworkTrafficAnalysisRequest**](UpdateNetworkTrafficAnalysisRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

