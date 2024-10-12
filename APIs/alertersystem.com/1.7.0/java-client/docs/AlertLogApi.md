# AlertLogApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiAlertLogGetCollection**](AlertLogApi.md#apiAlertLogGetCollection) | **GET** /api/alert-log | Retrieves the collection of AlertLog resources. |
| [**apiAlertLogIdGet**](AlertLogApi.md#apiAlertLogIdGet) | **GET** /api/alert-log/{id} | Retrieves a AlertLog resource. |


<a id="apiAlertLogGetCollection"></a>
# **apiAlertLogGetCollection**
> List&lt;AlertLogGet&gt; apiAlertLogGetCollection(page, dataSegmentCode, dataSegmentCode2, monitor, monitor2, alertService, alertService2, alertLogStatusCode, alertLogStatusCode2, partition, partition2, properties)

Retrieves the collection of AlertLog resources.

Retrieves the collection of AlertLog resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertLogApi apiInstance = new AlertLogApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String monitor = "monitor_example"; // String | 
    List<String> monitor2 = Arrays.asList(); // List<String> | 
    String alertService = "alertService_example"; // String | 
    List<String> alertService2 = Arrays.asList(); // List<String> | 
    String alertLogStatusCode = "alertLogStatusCode_example"; // String | 
    List<String> alertLogStatusCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<AlertLogGet> result = apiInstance.apiAlertLogGetCollection(page, dataSegmentCode, dataSegmentCode2, monitor, monitor2, alertService, alertService2, alertLogStatusCode, alertLogStatusCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertLogApi#apiAlertLogGetCollection");
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
| **alertService** | **String**|  | [optional] |
| **alertService2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **alertLogStatusCode** | **String**|  | [optional] |
| **alertLogStatusCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;AlertLogGet&gt;**](AlertLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertLog collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiAlertLogIdGet"></a>
# **apiAlertLogIdGet**
> AlertLogGet apiAlertLogIdGet(id)

Retrieves a AlertLog resource.

Retrieves a AlertLog resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertLogApi apiInstance = new AlertLogApi(defaultClient);
    String id = "id_example"; // String | AlertLog identifier
    try {
      AlertLogGet result = apiInstance.apiAlertLogIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertLogApi#apiAlertLogIdGet");
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
| **id** | **String**| AlertLog identifier | |

### Return type

[**AlertLogGet**](AlertLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertLog resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

