# MonitorStatusLogApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiMonitorStatusLogGetCollection**](MonitorStatusLogApi.md#apiMonitorStatusLogGetCollection) | **GET** /api/monitor-status-log | Retrieves the collection of MonitorStatusLog resources. |
| [**apiMonitorStatusLogIdGet**](MonitorStatusLogApi.md#apiMonitorStatusLogIdGet) | **GET** /api/monitor-status-log/{id} | Retrieves a MonitorStatusLog resource. |


<a id="apiMonitorStatusLogGetCollection"></a>
# **apiMonitorStatusLogGetCollection**
> List&lt;MonitorStatusLogGet&gt; apiMonitorStatusLogGetCollection(page, dataSegmentCode, dataSegmentCode2, monitor, monitor2, monitorStatusCode, monitorStatusCode2, partition, partition2, properties)

Retrieves the collection of MonitorStatusLog resources.

Retrieves the collection of MonitorStatusLog resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorStatusLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorStatusLogApi apiInstance = new MonitorStatusLogApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String monitor = "monitor_example"; // String | 
    List<String> monitor2 = Arrays.asList(); // List<String> | 
    String monitorStatusCode = "monitorStatusCode_example"; // String | 
    List<String> monitorStatusCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<MonitorStatusLogGet> result = apiInstance.apiMonitorStatusLogGetCollection(page, dataSegmentCode, dataSegmentCode2, monitor, monitor2, monitorStatusCode, monitorStatusCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorStatusLogApi#apiMonitorStatusLogGetCollection");
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
| **dataSegmentCode** | **String**|  | [optional] |
| **dataSegmentCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **monitor** | **String**|  | [optional] |
| **monitor2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **monitorStatusCode** | **String**|  | [optional] |
| **monitorStatusCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;MonitorStatusLogGet&gt;**](MonitorStatusLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorStatusLog collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiMonitorStatusLogIdGet"></a>
# **apiMonitorStatusLogIdGet**
> MonitorStatusLogGet apiMonitorStatusLogIdGet(id)

Retrieves a MonitorStatusLog resource.

Retrieves a MonitorStatusLog resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorStatusLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MonitorStatusLogApi apiInstance = new MonitorStatusLogApi(defaultClient);
    String id = "id_example"; // String | MonitorStatusLog identifier
    try {
      MonitorStatusLogGet result = apiInstance.apiMonitorStatusLogIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorStatusLogApi#apiMonitorStatusLogIdGet");
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
| **id** | **String**| MonitorStatusLog identifier | |

### Return type

[**MonitorStatusLogGet**](MonitorStatusLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | MonitorStatusLog resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

