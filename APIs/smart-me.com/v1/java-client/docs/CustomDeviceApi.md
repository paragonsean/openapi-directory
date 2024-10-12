# CustomDeviceApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCustomDeviceIdGet**](CustomDeviceApi.md#apiCustomDeviceIdGet) | **GET** /api/CustomDevice/{id} | Gets a Custom Device by it&#39;s ID |
| [**customDeviceGet**](CustomDeviceApi.md#customDeviceGet) | **GET** /api/CustomDevice | Gets all Custom Devices |
| [**customDevicePost**](CustomDeviceApi.md#customDevicePost) | **POST** /api/CustomDevice | Creates or updates a Custom Device or updates it&#39;s values. |


<a id="apiCustomDeviceIdGet"></a>
# **apiCustomDeviceIdGet**
> CustomDeviceToPost apiCustomDeviceIdGet(id)

Gets a Custom Device by it&#39;s ID

Gets a Device by it&#39;s ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    CustomDeviceApi apiInstance = new CustomDeviceApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    try {
      CustomDeviceToPost result = apiInstance.apiCustomDeviceIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDeviceApi#apiCustomDeviceIdGet");
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

[**CustomDeviceToPost**](CustomDeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customDeviceGet"></a>
# **customDeviceGet**
> List&lt;CustomDeviceToPost&gt; customDeviceGet()

Gets all Custom Devices

Gets all Devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    CustomDeviceApi apiInstance = new CustomDeviceApi(defaultClient);
    try {
      List<CustomDeviceToPost> result = apiInstance.customDeviceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDeviceApi#customDeviceGet");
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

[**List&lt;CustomDeviceToPost&gt;**](CustomDeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customDevicePost"></a>
# **customDevicePost**
> CustomDeviceToPost customDevicePost(customDeviceToPost)

Creates or updates a Custom Device or updates it&#39;s values.

Creates or updates a Custom Device or updates it&#39;s values.              A Custom Device can be any device that like to add some measurement values to the smart-me Cloud.              Only use a custom device for all non meters.              For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    CustomDeviceApi apiInstance = new CustomDeviceApi(defaultClient);
    CustomDeviceToPost customDeviceToPost = new CustomDeviceToPost(); // CustomDeviceToPost | Device object with all the data
    try {
      CustomDeviceToPost result = apiInstance.customDevicePost(customDeviceToPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDeviceApi#customDevicePost");
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
| **customDeviceToPost** | [**CustomDeviceToPost**](CustomDeviceToPost.md)| Device object with all the data | |

### Return type

[**CustomDeviceToPost**](CustomDeviceToPost.md)

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

