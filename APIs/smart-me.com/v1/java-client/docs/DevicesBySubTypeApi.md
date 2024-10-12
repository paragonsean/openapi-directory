# DevicesBySubTypeApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicesBySubTypeGet**](DevicesBySubTypeApi.md#devicesBySubTypeGet) | **GET** /api/DevicesBySubType | Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station) |


<a id="devicesBySubTypeGet"></a>
# **devicesBySubTypeGet**
> List&lt;Device&gt; devicesBySubTypeGet(meterSubType)

Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesBySubTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesBySubTypeApi apiInstance = new DevicesBySubTypeApi(defaultClient);
    String meterSubType = "MeterSubTypeUnknown"; // String | 
    try {
      List<Device> result = apiInstance.devicesBySubTypeGet(meterSubType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesBySubTypeApi#devicesBySubTypeGet");
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
| **meterSubType** | **String**|  | [enum: MeterSubTypeUnknown, MeterSubTypeCold, MeterSubTypeHeat, MeterSubTypeChargingStation, MeterSubTypeElectricity, MeterSubTypeWater, MeterSubTypeGas, MeterSubTypeElectricityHeat, MeterSubTypeTemperature, MeterSubTypeVirtualBattery] |

### Return type

[**List&lt;Device&gt;**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

