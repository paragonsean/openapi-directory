# ConfigurationApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configurationDelete**](ConfigurationApi.md#configurationDelete) | **DELETE** /system/configuration/{key} | Delete a configuration item. |
| [**configurationGet**](ConfigurationApi.md#configurationGet) | **GET** /system/configuration/{key} | Get the value of a configuration item. |
| [**configurationList**](ConfigurationApi.md#configurationList) | **GET** /system/configuration | Get the current system configuration. |


<a id="configurationDelete"></a>
# **configurationDelete**
> configurationDelete(key)

Delete a configuration item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String key = "key_example"; // String | The key of the configuration item to remove.
    try {
      apiInstance.configurationDelete(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationDelete");
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
| **key** | **String**| The key of the configuration item to remove. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The change has been accepted, and will take effect when the service can cleanly restart. |  -  |
| **404** | The configuration item does not exist. |  -  |
| **500** | An internal error is preventing deletion of the configuration item. |  -  |

<a id="configurationGet"></a>
# **configurationGet**
> Object configurationGet(key)

Get the value of a configuration item.

The response content may vary based on the configuration item&#39;s data type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String key = "key_example"; // String | The key of the configuration item.
    try {
      Object result = apiInstance.configurationGet(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationGet");
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
| **key** | **String**| The key of the configuration item. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value of the configuration item. |  -  |
| **404** | The configuration item does not exist. |  -  |

<a id="configurationList"></a>
# **configurationList**
> Map&lt;String, Object&gt; configurationList()

Get the current system configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.configurationList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#configurationList");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current system configuration. |  -  |

