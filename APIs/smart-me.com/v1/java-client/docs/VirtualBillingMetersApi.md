# VirtualBillingMetersApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualBillingMetersGet**](VirtualBillingMetersApi.md#virtualBillingMetersGet) | **GET** /api/VirtualBillingMeters | Beta: Gets all Meters available to activate as a Virtual Meter. |


<a id="virtualBillingMetersGet"></a>
# **virtualBillingMetersGet**
> List&lt;Device&gt; virtualBillingMetersGet()

Beta: Gets all Meters available to activate as a Virtual Meter.

Beta: Gets all Meters available to activate as a Virtual Meter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualBillingMetersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualBillingMetersApi apiInstance = new VirtualBillingMetersApi(defaultClient);
    try {
      List<Device> result = apiInstance.virtualBillingMetersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualBillingMetersApi#virtualBillingMetersGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

