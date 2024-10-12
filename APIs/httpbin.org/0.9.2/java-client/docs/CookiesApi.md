# CookiesApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cookiesDeleteGet**](CookiesApi.md#cookiesDeleteGet) | **GET** /cookies/delete | Deletes cookie(s) as provided by the query string and redirects to cookie list. |
| [**cookiesGet**](CookiesApi.md#cookiesGet) | **GET** /cookies | Returns cookie data. |
| [**cookiesSetGet**](CookiesApi.md#cookiesSetGet) | **GET** /cookies/set | Sets cookie(s) as provided by the query string and redirects to cookie list. |
| [**cookiesSetNameValueGet**](CookiesApi.md#cookiesSetNameValueGet) | **GET** /cookies/set/{name}/{value} | Sets a cookie and redirects to cookie list. |


<a id="cookiesDeleteGet"></a>
# **cookiesDeleteGet**
> cookiesDeleteGet(freeform)

Deletes cookie(s) as provided by the query string and redirects to cookie list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CookiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    CookiesApi apiInstance = new CookiesApi(defaultClient);
    Map<String, String> freeform = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.cookiesDeleteGet(freeform);
    } catch (ApiException e) {
      System.err.println("Exception when calling CookiesApi#cookiesDeleteGet");
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
| **freeform** | [**Map&lt;String, String&gt;**](String.md)|  | [optional] |

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
| **200** | Redirect to cookie list |  -  |

<a id="cookiesGet"></a>
# **cookiesGet**
> cookiesGet()

Returns cookie data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CookiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    CookiesApi apiInstance = new CookiesApi(defaultClient);
    try {
      apiInstance.cookiesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CookiesApi#cookiesGet");
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
| **200** | Set cookies. |  -  |

<a id="cookiesSetGet"></a>
# **cookiesSetGet**
> cookiesSetGet(freeform)

Sets cookie(s) as provided by the query string and redirects to cookie list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CookiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    CookiesApi apiInstance = new CookiesApi(defaultClient);
    Map<String, String> freeform = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.cookiesSetGet(freeform);
    } catch (ApiException e) {
      System.err.println("Exception when calling CookiesApi#cookiesSetGet");
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
| **freeform** | [**Map&lt;String, String&gt;**](String.md)|  | [optional] |

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
| **200** | Redirect to cookie list |  -  |

<a id="cookiesSetNameValueGet"></a>
# **cookiesSetNameValueGet**
> cookiesSetNameValueGet(name, value)

Sets a cookie and redirects to cookie list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CookiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    CookiesApi apiInstance = new CookiesApi(defaultClient);
    String name = "name_example"; // String | 
    String value = "value_example"; // String | 
    try {
      apiInstance.cookiesSetNameValueGet(name, value);
    } catch (ApiException e) {
      System.err.println("Exception when calling CookiesApi#cookiesSetNameValueGet");
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
| **name** | **String**|  | |
| **value** | **String**|  | |

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
| **200** | Set cookies and redirects to cookie list. |  -  |

