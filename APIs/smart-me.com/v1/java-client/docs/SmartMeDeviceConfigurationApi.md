# SmartMeDeviceConfigurationApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**smartMeDeviceConfigurationGet**](SmartMeDeviceConfigurationApi.md#smartMeDeviceConfigurationGet) | **GET** /api/SmartMeDeviceConfiguration/{id} | Gets the configuration of a smart-me device. |
| [**smartMeDeviceConfigurationPost**](SmartMeDeviceConfigurationApi.md#smartMeDeviceConfigurationPost) | **POST** /api/SmartMeDeviceConfiguration | Sets the configuration of a smart-me device. The device needs to be online. |


<a id="smartMeDeviceConfigurationGet"></a>
# **smartMeDeviceConfigurationGet**
> SmartMeDeviceConfigurationContainer smartMeDeviceConfigurationGet(id)

Gets the configuration of a smart-me device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartMeDeviceConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    SmartMeDeviceConfigurationApi apiInstance = new SmartMeDeviceConfigurationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      SmartMeDeviceConfigurationContainer result = apiInstance.smartMeDeviceConfigurationGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartMeDeviceConfigurationApi#smartMeDeviceConfigurationGet");
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

[**SmartMeDeviceConfigurationContainer**](SmartMeDeviceConfigurationContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="smartMeDeviceConfigurationPost"></a>
# **smartMeDeviceConfigurationPost**
> smartMeDeviceConfigurationPost(smartMeDeviceConfigurationContainer)

Sets the configuration of a smart-me device. The device needs to be online.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartMeDeviceConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    SmartMeDeviceConfigurationApi apiInstance = new SmartMeDeviceConfigurationApi(defaultClient);
    SmartMeDeviceConfigurationContainer smartMeDeviceConfigurationContainer = new SmartMeDeviceConfigurationContainer(); // SmartMeDeviceConfigurationContainer | 
    try {
      apiInstance.smartMeDeviceConfigurationPost(smartMeDeviceConfigurationContainer);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartMeDeviceConfigurationApi#smartMeDeviceConfigurationPost");
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
| **smartMeDeviceConfigurationContainer** | [**SmartMeDeviceConfigurationContainer**](SmartMeDeviceConfigurationContainer.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

