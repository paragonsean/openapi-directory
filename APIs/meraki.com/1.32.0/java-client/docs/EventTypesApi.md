# EventTypesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkEventsEventTypes_2**](EventTypesApi.md#getNetworkEventsEventTypes_2) | **GET** /networks/{networkId}/events/eventTypes | List the event type to human-readable description |


<a id="getNetworkEventsEventTypes_2"></a>
# **getNetworkEventsEventTypes_2**
> List&lt;GetNetworkEventsEventTypes200ResponseInner&gt; getNetworkEventsEventTypes_2(networkId)

List the event type to human-readable description

List the event type to human-readable description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EventTypesApi apiInstance = new EventTypesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkEventsEventTypes200ResponseInner> result = apiInstance.getNetworkEventsEventTypes_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypesApi#getNetworkEventsEventTypes_2");
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

[**List&lt;GetNetworkEventsEventTypes200ResponseInner&gt;**](GetNetworkEventsEventTypes200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

