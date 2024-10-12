# ChannelUtilizationHistoryApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkWirelessChannelUtilizationHistory_1**](ChannelUtilizationHistoryApi.md#getNetworkWirelessChannelUtilizationHistory_1) | **GET** /networks/{networkId}/wireless/channelUtilizationHistory | Return AP channel utilization over time for a device or network client |


<a id="getNetworkWirelessChannelUtilizationHistory_1"></a>
# **getNetworkWirelessChannelUtilizationHistory_1**
> List&lt;GetNetworkWirelessChannelUtilizationHistory200ResponseInner&gt; getNetworkWirelessChannelUtilizationHistory_1(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band)

Return AP channel utilization over time for a device or network client

Return AP channel utilization over time for a device or network client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelUtilizationHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ChannelUtilizationHistoryApi apiInstance = new ChannelUtilizationHistoryApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
    Boolean autoResolution = true; // Boolean | Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    String clientId = "clientId_example"; // String | Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
    String deviceSerial = "deviceSerial_example"; // String | Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
    String apTag = "apTag_example"; // String | Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6').
    try {
      List<GetNetworkWirelessChannelUtilizationHistory200ResponseInner> result = apiInstance.getNetworkWirelessChannelUtilizationHistory_1(networkId, t0, t1, timespan, resolution, autoResolution, clientId, deviceSerial, apTag, band);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelUtilizationHistoryApi#getNetworkWirelessChannelUtilizationHistory_1");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400. | [optional] |
| **autoResolution** | **Boolean**| Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false. | [optional] |
| **clientId** | **String**| Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client&#39;s connection history. | [optional] |
| **deviceSerial** | **String**| Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified. | [optional] |
| **apTag** | **String**| Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). | [optional] [enum: 2.4, 5, 6] |

### Return type

[**List&lt;GetNetworkWirelessChannelUtilizationHistory200ResponseInner&gt;**](GetNetworkWirelessChannelUtilizationHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

