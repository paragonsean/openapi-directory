# PicoSettingsApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**picoSettingsGet**](PicoSettingsApi.md#picoSettingsGet) | **GET** /api/pico/settings/{id} | GET: api/pico/settings                            Returns the settings of a pico charging station. |


<a id="picoSettingsGet"></a>
# **picoSettingsGet**
> PicoSettingsDto picoSettingsGet(id)

GET: api/pico/settings                            Returns the settings of a pico charging station.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoSettingsApi apiInstance = new PicoSettingsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      PicoSettingsDto result = apiInstance.picoSettingsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoSettingsApi#picoSettingsGet");
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

[**PicoSettingsDto**](PicoSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

