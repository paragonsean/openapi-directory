# MonitorStatusCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMonitorStatusCodeGetCollection**](MonitorStatusCodeApi.md#apiMonitorStatusCodeGetCollection) | **GET** /api/monitor-status-code | Retrieves the collection of MonitorStatusCode resources. |
| [**apiMonitorStatusCodeIdGet**](MonitorStatusCodeApi.md#apiMonitorStatusCodeIdGet) | **GET** /api/monitor-status-code/{id} | Retrieves a MonitorStatusCode resource. |


<a id="apiMonitorStatusCodeGetCollection"></a>
# **apiMonitorStatusCodeGetCollection**
> List&lt;MonitorStatusCodeGet&gt; apiMonitorStatusCodeGetCollection(page, properties)

Retrieves the collection of MonitorStatusCode resources.

Retrieves the collection of MonitorStatusCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorStatusCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorStatusCodeApi apiInstance = new MonitorStatusCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<MonitorStatusCodeGet> result = apiInstance.apiMonitorStatusCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorStatusCodeApi#apiMonitorStatusCodeGetCollection");
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

[**List&lt;MonitorStatusCodeGet&gt;**](MonitorStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorStatusCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiMonitorStatusCodeIdGet"></a>
# **apiMonitorStatusCodeIdGet**
> MonitorStatusCodeGet apiMonitorStatusCodeIdGet(id)

Retrieves a MonitorStatusCode resource.

Retrieves a MonitorStatusCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorStatusCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorStatusCodeApi apiInstance = new MonitorStatusCodeApi(defaultClient);
    String id = "id_example"; // String | MonitorStatusCode identifier
    try {
      MonitorStatusCodeGet result = apiInstance.apiMonitorStatusCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorStatusCodeApi#apiMonitorStatusCodeIdGet");
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
| **id** | **String**| MonitorStatusCode identifier | |

### Return type

[**MonitorStatusCodeGet**](MonitorStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorStatusCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

