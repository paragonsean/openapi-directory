# KeysApiApi

All URIs are relative to *https://keyserv.solutions*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keysApiCurrent**](KeysApiApi.md#keysApiCurrent) | **GET** /v1/KeysApi/Current/{serial} |  |
| [**keysApiCustom**](KeysApiApi.md#keysApiCustom) | **GET** /v1/KeysApi/Custom/{serial} |  |
| [**keysApiExpiry**](KeysApiApi.md#keysApiExpiry) | **GET** /v1/KeysApi/Expiry/{serial} |  |
| [**keysApiFind**](KeysApiApi.md#keysApiFind) | **GET** /v1/KeysApi/Find/{serial} |  |


<a id="keysApiCurrent"></a>
# **keysApiCurrent**
> KeysApiCurrent200Response keysApiCurrent(serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    KeysApiApi apiInstance = new KeysApiApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      KeysApiCurrent200Response result = apiInstance.keysApiCurrent(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApiApi#keysApiCurrent");
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
| **serial** | **String**|  | |

### Return type

[**KeysApiCurrent200Response**](KeysApiCurrent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="keysApiCustom"></a>
# **keysApiCustom**
> File keysApiCustom(serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    KeysApiApi apiInstance = new KeysApiApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      File result = apiInstance.keysApiCustom(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApiApi#keysApiCustom");
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
| **serial** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="keysApiExpiry"></a>
# **keysApiExpiry**
> KeysApiExpiry200Response keysApiExpiry(serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    KeysApiApi apiInstance = new KeysApiApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      KeysApiExpiry200Response result = apiInstance.keysApiExpiry(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApiApi#keysApiExpiry");
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
| **serial** | **String**|  | |

### Return type

[**KeysApiExpiry200Response**](KeysApiExpiry200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="keysApiFind"></a>
# **keysApiFind**
> KeysApiFind200Response keysApiFind(serial)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    KeysApiApi apiInstance = new KeysApiApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      KeysApiFind200Response result = apiInstance.keysApiFind(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApiApi#keysApiFind");
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
| **serial** | **String**|  | |

### Return type

[**KeysApiFind200Response**](KeysApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

