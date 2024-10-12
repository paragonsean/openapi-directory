# RssApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1RssAllbillsRssGet**](RssApi.md#apiV1RssAllbillsRssGet) | **GET** /api/v1/Rss/allbills.rss | Returns an Rss feed of all Bills. |
| [**apiV1RssBillsIdRssGet**](RssApi.md#apiV1RssBillsIdRssGet) | **GET** /api/v1/Rss/Bills/{id}.rss | Returns an Rss feed of a certain Bill. |
| [**apiV1RssPrivatebillsRssGet**](RssApi.md#apiV1RssPrivatebillsRssGet) | **GET** /api/v1/Rss/privatebills.rss | Returns an Rss feed of private Bills. |
| [**apiV1RssPublicbillsRssGet**](RssApi.md#apiV1RssPublicbillsRssGet) | **GET** /api/v1/Rss/publicbills.rss | Returns an Rss feed of public Bills. |


<a id="apiV1RssAllbillsRssGet"></a>
# **apiV1RssAllbillsRssGet**
> apiV1RssAllbillsRssGet()

Returns an Rss feed of all Bills.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    RssApi apiInstance = new RssApi(defaultClient);
    try {
      apiInstance.apiV1RssAllbillsRssGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RssApi#apiV1RssAllbillsRssGet");
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
| **200** | Success |  -  |

<a id="apiV1RssBillsIdRssGet"></a>
# **apiV1RssBillsIdRssGet**
> apiV1RssBillsIdRssGet(id)

Returns an Rss feed of a certain Bill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    RssApi apiInstance = new RssApi(defaultClient);
    Integer id = 56; // Integer | Id of Bill
    try {
      apiInstance.apiV1RssBillsIdRssGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RssApi#apiV1RssBillsIdRssGet");
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
| **id** | **Integer**| Id of Bill | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiV1RssPrivatebillsRssGet"></a>
# **apiV1RssPrivatebillsRssGet**
> apiV1RssPrivatebillsRssGet()

Returns an Rss feed of private Bills.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    RssApi apiInstance = new RssApi(defaultClient);
    try {
      apiInstance.apiV1RssPrivatebillsRssGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RssApi#apiV1RssPrivatebillsRssGet");
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
| **200** | Success |  -  |

<a id="apiV1RssPublicbillsRssGet"></a>
# **apiV1RssPublicbillsRssGet**
> apiV1RssPublicbillsRssGet()

Returns an Rss feed of public Bills.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RssApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    RssApi apiInstance = new RssApi(defaultClient);
    try {
      apiInstance.apiV1RssPublicbillsRssGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RssApi#apiV1RssPublicbillsRssGet");
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
| **200** | Success |  -  |

