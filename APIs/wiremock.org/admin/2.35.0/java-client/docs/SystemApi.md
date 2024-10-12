# SystemApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminResetPost**](SystemApi.md#adminResetPost) | **POST** /__admin/reset | Reset mappings and request journal |
| [**adminSettingsPost**](SystemApi.md#adminSettingsPost) | **POST** /__admin/settings | Update global settings |
| [**adminShutdownPost**](SystemApi.md#adminShutdownPost) | **POST** /__admin/shutdown |  |


<a id="adminResetPost"></a>
# **adminResetPost**
> adminResetPost()

Reset mappings and request journal

Reset mappings to the default state and reset the request journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      apiInstance.adminResetPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#adminResetPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully reset |  -  |

<a id="adminSettingsPost"></a>
# **adminSettingsPost**
> adminSettingsPost(adminSettingsPostRequest)

Update global settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    AdminSettingsPostRequest adminSettingsPostRequest = new AdminSettingsPostRequest(); // AdminSettingsPostRequest | 
    try {
      apiInstance.adminSettingsPost(adminSettingsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#adminSettingsPost");
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
| **adminSettingsPostRequest** | [**AdminSettingsPostRequest**](AdminSettingsPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings successfully updated |  -  |

<a id="adminShutdownPost"></a>
# **adminShutdownPost**
> adminShutdownPost()



Shutdown the WireMock server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      apiInstance.adminShutdownPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#adminShutdownPost");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server will be shut down |  -  |

