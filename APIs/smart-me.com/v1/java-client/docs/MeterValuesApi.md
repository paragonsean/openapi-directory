# MeterValuesApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meterValuesGet**](MeterValuesApi.md#meterValuesGet) | **GET** /api/MeterValues/{id} | Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned. |


<a id="meterValuesGet"></a>
# **meterValuesGet**
> DeviceInPast meterValuesGet(id, date)

Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned.

Gets the Values for a Meter at a given Date. The first Value found before the given Date is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeterValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    MeterValuesApi apiInstance = new MeterValuesApi(defaultClient);
    String id = "id_example"; // String | 
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      DeviceInPast result = apiInstance.meterValuesGet(id, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeterValuesApi#meterValuesGet");
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
| **date** | **OffsetDateTime**|  | |

### Return type

[**DeviceInPast**](DeviceInPast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

