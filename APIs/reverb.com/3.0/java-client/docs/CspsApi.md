# CspsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cspsCategoriesGet**](CspsApi.md#cspsCategoriesGet) | **GET** /csps/categories |  |
| [**cspsFindGet**](CspsApi.md#cspsFindGet) | **GET** /csps/find | Show comparison shopping page |
| [**cspsGet**](CspsApi.md#cspsGet) | **GET** /csps | Returns a set of comparison shopping pages based on the current params |
| [**cspsIdGet**](CspsApi.md#cspsIdGet) | **GET** /csps/{id} |  |


<a id="cspsCategoriesGet"></a>
# **cspsCategoriesGet**
> cspsCategoriesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CspsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    CspsApi apiInstance = new CspsApi(defaultClient);
    try {
      apiInstance.cspsCategoriesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CspsApi#cspsCategoriesGet");
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
| **0** | Unexpected error |  -  |

<a id="cspsFindGet"></a>
# **cspsFindGet**
> cspsFindGet(id, slug)

Show comparison shopping page

Show comparison shopping page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CspsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    CspsApi apiInstance = new CspsApi(defaultClient);
    String id = "id_example"; // String | ID of the comparison shopping page
    String slug = "slug_example"; // String | Slug of the comparison shopping page
    try {
      apiInstance.cspsFindGet(id, slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling CspsApi#cspsFindGet");
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
| **id** | **String**| ID of the comparison shopping page | [optional] |
| **slug** | **String**| Slug of the comparison shopping page | [optional] |

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
| **0** | Unexpected error |  -  |

<a id="cspsGet"></a>
# **cspsGet**
> cspsGet()

Returns a set of comparison shopping pages based on the current params

Returns a set of comparison shopping pages based on the current params

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CspsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    CspsApi apiInstance = new CspsApi(defaultClient);
    try {
      apiInstance.cspsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CspsApi#cspsGet");
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
| **0** | Unexpected error |  -  |

<a id="cspsIdGet"></a>
# **cspsIdGet**
> cspsIdGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CspsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    CspsApi apiInstance = new CspsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.cspsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CspsApi#cspsIdGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

