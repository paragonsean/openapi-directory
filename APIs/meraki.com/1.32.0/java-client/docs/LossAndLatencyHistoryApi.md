# LossAndLatencyHistoryApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceLossAndLatencyHistory_2**](LossAndLatencyHistoryApi.md#getDeviceLossAndLatencyHistory_2) | **GET** /devices/{serial}/lossAndLatencyHistory | Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device. |


<a id="getDeviceLossAndLatencyHistory_2"></a>
# **getDeviceLossAndLatencyHistory_2**
> List&lt;Object&gt; getDeviceLossAndLatencyHistory_2(serial, ip, t0, t1, timespan, resolution, uplink)

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LossAndLatencyHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LossAndLatencyHistoryApi apiInstance = new LossAndLatencyHistoryApi(defaultClient);
    String serial = "serial_example"; // String | 
    String ip = "ip_example"; // String | The destination IP used to obtain the requested stats. This is required.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    String uplink = "cellular"; // String | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    try {
      List<Object> result = apiInstance.getDeviceLossAndLatencyHistory_2(serial, ip, t0, t1, timespan, resolution, uplink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LossAndLatencyHistoryApi#getDeviceLossAndLatencyHistory_2");
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
| **serial** | **String**|  | |
| **ip** | **String**| The destination IP used to obtain the requested stats. This is required. | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 60 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. | [optional] |
| **uplink** | **String**| The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1. | [optional] [enum: cellular, wan1, wan2] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

