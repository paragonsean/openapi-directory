# TrackingApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTrack**](TrackingApi.md#getTrack) | **GET** /track | Tracking |


<a id="getTrack"></a>
# **getTrack**
> TrackingResponse getTrack(trackingNumber)

Tracking

Get uniformed tracking events for any package, this response is carrier independent. Please note, an API Key is required for throttling purposes, please contact your success manager for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fulfillment.com/v2");

    TrackingApi apiInstance = new TrackingApi(defaultClient);
    String trackingNumber = "trackingNumber_example"; // String | 
    try {
      TrackingResponse result = apiInstance.getTrack(trackingNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrackingApi#getTrack");
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
| **trackingNumber** | **String**|  | [optional] |

### Return type

[**TrackingResponse**](TrackingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **429** | Too Many Requests |  -  |

