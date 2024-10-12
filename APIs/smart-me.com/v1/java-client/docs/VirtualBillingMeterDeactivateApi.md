# VirtualBillingMeterDeactivateApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualBillingMeterDeactivatePost**](VirtualBillingMeterDeactivateApi.md#virtualBillingMeterDeactivatePost) | **POST** /api/VirtualBillingMeterDeactivate | Beta: Virtual Meter API: Deactivates a Virtual Meter. |


<a id="virtualBillingMeterDeactivatePost"></a>
# **virtualBillingMeterDeactivatePost**
> Object virtualBillingMeterDeactivatePost(vmeterToDeactivate)

Beta: Virtual Meter API: Deactivates a Virtual Meter.

Beta: Virtual Meter API: Deactivates a Virtual Meter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualBillingMeterDeactivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualBillingMeterDeactivateApi apiInstance = new VirtualBillingMeterDeactivateApi(defaultClient);
    VMeterToDeactivate vmeterToDeactivate = new VMeterToDeactivate(); // VMeterToDeactivate | The Meter to activate
    try {
      Object result = apiInstance.virtualBillingMeterDeactivatePost(vmeterToDeactivate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualBillingMeterDeactivateApi#virtualBillingMeterDeactivatePost");
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
| **vmeterToDeactivate** | [**VMeterToDeactivate**](VMeterToDeactivate.md)| The Meter to activate | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

