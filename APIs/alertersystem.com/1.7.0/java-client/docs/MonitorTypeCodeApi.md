# MonitorTypeCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMonitorTypeCodeGetCollection**](MonitorTypeCodeApi.md#apiMonitorTypeCodeGetCollection) | **GET** /api/monitor-type-code | Retrieves the collection of MonitorTypeCode resources. |
| [**apiMonitorTypeCodeIdGet**](MonitorTypeCodeApi.md#apiMonitorTypeCodeIdGet) | **GET** /api/monitor-type-code/{id} | Retrieves a MonitorTypeCode resource. |


<a id="apiMonitorTypeCodeGetCollection"></a>
# **apiMonitorTypeCodeGetCollection**
> List&lt;MonitorTypeCodeGet&gt; apiMonitorTypeCodeGetCollection(page, properties)

Retrieves the collection of MonitorTypeCode resources.

Retrieves the collection of MonitorTypeCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorTypeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorTypeCodeApi apiInstance = new MonitorTypeCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<MonitorTypeCodeGet> result = apiInstance.apiMonitorTypeCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorTypeCodeApi#apiMonitorTypeCodeGetCollection");
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

[**List&lt;MonitorTypeCodeGet&gt;**](MonitorTypeCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorTypeCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiMonitorTypeCodeIdGet"></a>
# **apiMonitorTypeCodeIdGet**
> MonitorTypeCodeGet apiMonitorTypeCodeIdGet(id)

Retrieves a MonitorTypeCode resource.

Retrieves a MonitorTypeCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorTypeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorTypeCodeApi apiInstance = new MonitorTypeCodeApi(defaultClient);
    String id = "id_example"; // String | MonitorTypeCode identifier
    try {
      MonitorTypeCodeGet result = apiInstance.apiMonitorTypeCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorTypeCodeApi#apiMonitorTypeCodeIdGet");
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
| **id** | **String**| MonitorTypeCode identifier | |

### Return type

[**MonitorTypeCodeGet**](MonitorTypeCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorTypeCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

