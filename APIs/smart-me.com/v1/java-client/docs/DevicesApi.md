# DevicesApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDevicesIdGet**](DevicesApi.md#apiDevicesIdGet) | **GET** /api/Devices/{id} | Gets a Device by it&#39;s ID |
| [**devicesGet**](DevicesApi.md#devicesGet) | **GET** /api/Devices | Gets all Devices |
| [**devicesPost**](DevicesApi.md#devicesPost) | **POST** /api/Devices | Creates or updates a Device or updates it&#39;s values. |
| [**devicesPut**](DevicesApi.md#devicesPut) | **PUT** /api/Devices/{id} | Updates the On/Off Switch on a device.               For new implementations please use the \&quot;actions\&quot; command |


<a id="apiDevicesIdGet"></a>
# **apiDevicesIdGet**
> Device apiDevicesIdGet(id)

Gets a Device by it&#39;s ID

Gets a Device by it&#39;s ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    try {
      Device result = apiInstance.apiDevicesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#apiDevicesIdGet");
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
| **id** | **String**| The ID of the device | |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="devicesGet"></a>
# **devicesGet**
> List&lt;Device&gt; devicesGet()

Gets all Devices

Gets all Devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    try {
      List<Device> result = apiInstance.devicesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGet");
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

<a id="devicesPost"></a>
# **devicesPost**
> DeviceToPost devicesPost(deviceToPost)

Creates or updates a Device or updates it&#39;s values.

Creates or updates a Device or updates it&#39;s values.               For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    DeviceToPost deviceToPost = new DeviceToPost(); // DeviceToPost | Device object with all the data
    try {
      DeviceToPost result = apiInstance.devicesPost(deviceToPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesPost");
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
| **deviceToPost** | [**DeviceToPost**](DeviceToPost.md)| Device object with all the data | |

### Return type

[**DeviceToPost**](DeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="devicesPut"></a>
# **devicesPut**
> Object devicesPut(id, switchState, switchNumber)

Updates the On/Off Switch on a device.               For new implementations please use the \&quot;actions\&quot; command

Updates the On/Off Switch on a device              For new implementations please use the \&quot;actions\&quot; command

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    Boolean switchState = true; // Boolean | The new state of the switch
    Integer switchNumber = 56; // Integer | The number of the switch if there are multiple (1 for L1, 3 for L3)
    try {
      Object result = apiInstance.devicesPut(id, switchState, switchNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesPut");
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
| **id** | **String**| The ID of the device | |
| **switchState** | **Boolean**| The new state of the switch | |
| **switchNumber** | **Integer**| The number of the switch if there are multiple (1 for L1, 3 for L3) | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **405** | MethodNotAllowed |  -  |

