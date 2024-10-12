# PicoChargingHistoryApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**picoChargingHistoryGet**](PicoChargingHistoryApi.md#picoChargingHistoryGet) | **GET** /api/pico/history/{id} | Gets the last charging history for a pico station |


<a id="picoChargingHistoryGet"></a>
# **picoChargingHistoryGet**
> List&lt;PicoChargingHistoryData&gt; picoChargingHistoryGet(id)

Gets the last charging history for a pico station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoChargingHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoChargingHistoryApi apiInstance = new PicoChargingHistoryApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<PicoChargingHistoryData> result = apiInstance.picoChargingHistoryGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoChargingHistoryApi#picoChargingHistoryGet");
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
| **id** | **String**|  | |

### Return type

[**List&lt;PicoChargingHistoryData&gt;**](PicoChargingHistoryData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

