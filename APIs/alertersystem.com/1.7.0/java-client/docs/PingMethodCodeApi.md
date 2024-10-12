# PingMethodCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPingMethodCodeGetCollection**](PingMethodCodeApi.md#apiPingMethodCodeGetCollection) | **GET** /api/ping-method-code | Retrieves the collection of PingMethodCode resources. |
| [**apiPingMethodCodeIdGet**](PingMethodCodeApi.md#apiPingMethodCodeIdGet) | **GET** /api/ping-method-code/{id} | Retrieves a PingMethodCode resource. |


<a id="apiPingMethodCodeGetCollection"></a>
# **apiPingMethodCodeGetCollection**
> List&lt;PingMethodCodeGet&gt; apiPingMethodCodeGetCollection(page, properties)

Retrieves the collection of PingMethodCode resources.

Retrieves the collection of PingMethodCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingMethodCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PingMethodCodeApi apiInstance = new PingMethodCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<PingMethodCodeGet> result = apiInstance.apiPingMethodCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingMethodCodeApi#apiPingMethodCodeGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;PingMethodCodeGet&gt;**](PingMethodCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PingMethodCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiPingMethodCodeIdGet"></a>
# **apiPingMethodCodeIdGet**
> PingMethodCodeGet apiPingMethodCodeIdGet(id)

Retrieves a PingMethodCode resource.

Retrieves a PingMethodCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingMethodCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    PingMethodCodeApi apiInstance = new PingMethodCodeApi(defaultClient);
    String id = "id_example"; // String | PingMethodCode identifier
    try {
      PingMethodCodeGet result = apiInstance.apiPingMethodCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingMethodCodeApi#apiPingMethodCodeIdGet");
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
| **id** | **String**| PingMethodCode identifier | |

### Return type

[**PingMethodCodeGet**](PingMethodCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PingMethodCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

