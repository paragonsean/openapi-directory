# DevicesByEnergyApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicesByEnergyGet**](DevicesByEnergyApi.md#devicesByEnergyGet) | **GET** /api/DevicesByEnergy | Gets all Devices for an Energy Type |


<a id="devicesByEnergyGet"></a>
# **devicesByEnergyGet**
> List&lt;Device&gt; devicesByEnergyGet(meterEnergyType)

Gets all Devices for an Energy Type

Gets all Devices for an Energy Type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesByEnergyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesByEnergyApi apiInstance = new DevicesByEnergyApi(defaultClient);
    String meterEnergyType = "MeterTypeUnknown"; // String | 
    try {
      List<Device> result = apiInstance.devicesByEnergyGet(meterEnergyType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesByEnergyApi#devicesByEnergyGet");
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
| **meterEnergyType** | **String**|  | [enum: MeterTypeUnknown, MeterTypeElectricity, MeterTypeWater, MeterTypeGas, MeterTypeHeat, MeterTypeHCA, MeterTypeAllMeters, MeterTypeTemperature, MeterTypeMBusGateway, MeterTypeRS485Gateway, MeterTypeCustomDevice, MeterTypeCompressedAir, MeterTypeSolarLog, MeterTypeVirtualMeter, MeterTypeWMBusGateway] |

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

