# PicoChargingApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**picoChargingGet**](PicoChargingApi.md#picoChargingGet) | **GET** /api/pico/charging/{id} | Gets the active charging data of a pico station |


<a id="picoChargingGet"></a>
# **picoChargingGet**
> PicoChargingData picoChargingGet(id)

Gets the active charging data of a pico station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoChargingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoChargingApi apiInstance = new PicoChargingApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      PicoChargingData result = apiInstance.picoChargingGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoChargingApi#picoChargingGet");
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

[**PicoChargingData**](PicoChargingData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

