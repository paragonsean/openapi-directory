# VirtualBillingMeterActiveApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualBillingMeterActiveGet**](VirtualBillingMeterActiveApi.md#virtualBillingMeterActiveGet) | **GET** /api/VirtualBillingMeterActive | Beta: Gets all active virtual meters |
| [**virtualBillingMeterActivePost**](VirtualBillingMeterActiveApi.md#virtualBillingMeterActivePost) | **POST** /api/VirtualBillingMeterActive | Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User. |


<a id="virtualBillingMeterActiveGet"></a>
# **virtualBillingMeterActiveGet**
> List&lt;Device&gt; virtualBillingMeterActiveGet()

Beta: Gets all active virtual meters

Beta: Gets all active virtual meters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualBillingMeterActiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualBillingMeterActiveApi apiInstance = new VirtualBillingMeterActiveApi(defaultClient);
    try {
      List<Device> result = apiInstance.virtualBillingMeterActiveGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualBillingMeterActiveApi#virtualBillingMeterActiveGet");
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

<a id="virtualBillingMeterActivePost"></a>
# **virtualBillingMeterActivePost**
> Device virtualBillingMeterActivePost(vmeterToActivate)

Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualBillingMeterActiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualBillingMeterActiveApi apiInstance = new VirtualBillingMeterActiveApi(defaultClient);
    VMeterToActivate vmeterToActivate = new VMeterToActivate(); // VMeterToActivate | The Meter to activate
    try {
      Device result = apiInstance.virtualBillingMeterActivePost(vmeterToActivate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualBillingMeterActiveApi#virtualBillingMeterActivePost");
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
| **vmeterToActivate** | [**VMeterToActivate**](VMeterToActivate.md)| The Meter to activate | |

### Return type

[**Device**](Device.md)

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

